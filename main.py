# The code of the the whole system
# used to control the state machine
from gpiozero import MotionSensor
from gpiozero import LED
from state_machine import StateMachine
from threading import Timer
from repeatableTimer import RepeatableTimer
from adafruit_servokit import ServoKit
import time
import serial
import sys

# used for moving onto the next state of the state machine
# in a set period of time. Used with RepeatablTimer
def nextState():
    states.on_event('t')

# used for stoping the servo motor in a set period of time. 
# Is also used when sensor determines cat is in litter box. Used with RepeatablTimer
def StopServo():
    kit.continuous_servo[15].throttle = -0.11111105
    states.on_event('t')

# initialize the sensors, motors, and the state machine
port = serial.Serial("/dev/ttyAMA0", 115200)
pir = MotionSensor(21)
kit = ServoKit(channels=16)
states = StateMachine()

# initialize variables for use
t = 0
p = 0
Inverse_t = 0
Inverse_p = 0
prev_rv = 0
int_rv = 0

# set up all the Timer for later use in state machine
timer = RepeatableTimer(5, nextState)
timer2 = RepeatableTimer((10 - (p - t)), StopServo)
timer3 = RepeatableTimer((10 - (Inverse_p - Inverse_t)), StopServo)

# boolean for state machine, so Timer doesn't start more than once before cancel
timer_started = False
timer2_started = False
timer3_started = False
InSave_State = False
In_I_Save_State = False


while True:
    # used for gathering the data of the force sensor from the UART
    # to determine if the pressure changed or not
    prev_rv = int_rv
    value = 0
    for x in range(50):
        received_data = port.read(4)
        value += int.from_bytes(received_data,sys.byteorder)
    int_rv = value
    
    # this determines whether the pressure changes when cat stepped in
    if((int_rv/1000000) - (prev_rv/1000000) >= 10000):
        print("cat entering_pressure")
        states.on_event('p')
        if(timer_started == True):
            timer_started = False
            timer.cancel()
        if(timer2_started == True):
            timer2_started = False
            timer_started = False
            timer2.cancel()
        if(timer3_started == True):
            timer3_started = False
            timer3.cancel()
    
    # this determines whether the pressure changes when cat stepped out
    if((prev_rv/1000000) - (int_rv/1000000) >= 10000):
        print("cat leaving_pressure")
        states.on_event('o')
    
    # get the name of states for later action in state machine
    name = str(states.state)
    
    # Initial state used for resetting all variables and booleans
    if(name == "Initial"):
        timer_started = False
        timer2_started = False
        timer3_started = False
        InSaveState = False
        In_I_Save_State = False
        t = 0
        p = 0
        Inverse_t = 0
        Inverse_p = 0
    
    # wait a bit after cat leaves the the litter box
    if(name == "Wait5Sec" and timer_started == False):
        timer.start()
        timer_started = True
        InSaveState = False
        
    # start the motor for a limited amount of time for dumping the wastes
    if(name == "Operation" and timer2_started == False):
        kit.continuous_servo[15].throttle = 0.5
        timer2 = RepeatableTimer(10 - (p - t), StopServo)
        print(10 - (p - t))
        print(p - t)
        t = time.time()
        timer_started = False
        timer2.start()
        timer2_started = True
    
    # used for stopping the motor during a sense in the sensors
    if(name == "SaveState" and InSaveState == False):        
        p = time.time()
        kit.continuous_servo[15].throttle = -0.1111111
        InSaveState = True
    
    # used for putting the try back down, start the motor in reverse for a limited amount of time
    if(name == "InverseOperation" and timer3_started == False):
        kit.continuous_servo[15].throttle = -0.5
        timer3 = RepeatableTimer(10 - (Inverse_p - Inverse_t), StopServo)
        print(10 - (Inverse_p - Inverse_t))
        Inverse_t = time.time()
        timer_started = False
        timer3.start()
        timer3_started = True
    
    # wait for the cat to leave the box when in reverse mode
    if(name == "Wait5Sec_I" and timer_started == False):
        timer.start()
        timer_started = True
        In_I_Save_State = False
    
    # used for stopping the motor during a sense in the sensors when in reverse mode
    if(name == "Save_I_State" and In_I_Save_State == False):
        Inverse_p = time.time()
        kit.continuous_servo[15].throttle = -0.1111111
        In_I_Save_State = True
    
    # ignore the motion PIR sensor when motors are in operation
    if(name != "Operation" and name != "InverseOperation"):
        if pir.motion_detected:
             print("Motion detected")
             states.on_event('m')
             if(timer_started == True):
                 timer_started = False
                 timer.cancel()
             if(timer2_started == True):
                 timer2_started = False
                 timer_started = False
                 timer2.cancel()
             if(timer3_started == True):
                 timer3_started = False
                 timer3.cancel()
        else:
            # when in these states, have an extra input to determine if there is no motion
            # detected when a change in pressure is not detected
            if(name == "MotionOnly" or name == "MotionOnly_I"):
                print("No motion detected")
                states.on_event('n')
