from gpiozero import MotionSensor
from gpiozero import LED
from state_machine import StateMachine
from threading import Timer
from repeatableTimer import RepeatableTimer
from adafruit_servokit import ServoKit
#from func_timeout import *
import time
import serial
import sys

def nextState():
    states.on_event('t')
    
def StopServo():
    kit.continuous_servo[15].throttle = -0.11111105
    states.on_event('t')

port = serial.Serial("/dev/ttyAMA0", 115200)
pir = MotionSensor(21)

t = 0
p = 0
Inverse_t = 0
Inverse_p = 0
prev_rv = 0
int_rv = 0

timer = RepeatableTimer(5, nextState)
timer2 = RepeatableTimer((10 - (p - t)), StopServo)
timer3 = RepeatableTimer((10 - (Inverse_p - Inverse_t)), StopServo)

timer_started = False
timer2_started = False
timer3_started = False
InSave_State = False
In_I_Save_State = False

kit = ServoKit(channels=16)
states = StateMachine()

while True:
    prev_rv = int_rv
    #received_data = port.read(4)
    #time.sleep(0.01)
    #data_left = port.inWaiting()
    #received_data += port.read(data_left)
    value = 0
    for x in range(50):
        received_data = port.read(4)
        value += int.from_bytes(received_data,sys.byteorder)
    int_rv = value
    #print(int_rv/1000000)
    #print((prev_rv/1000000) - (int_rv/1000000))
    
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
            
    if((prev_rv/1000000) - (int_rv/1000000) >= 10000):
        print("cat leaving_pressure")
        states.on_event('o')
    
    name = str(states.state)
    
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
    
    if(name == "Wait5Sec" and timer_started == False):
        timer.start()
        timer_started = True
        InSaveState = False
        
    if(name == "Operation" and timer2_started == False):
        kit.continuous_servo[15].throttle = 0.5
        timer2 = RepeatableTimer(10 - (p - t), StopServo)
        print(10 - (p - t))
        print(p - t)
        t = time.time()
        timer_started = False
        timer2.start()
        timer2_started = True
    
    if(name == "SaveState" and InSaveState == False):        
        p = time.time()
        kit.continuous_servo[15].throttle = -0.1111111
        InSaveState = True
    
    if(name == "InverseOperation" and timer3_started == False):
        kit.continuous_servo[15].throttle = -0.5
        timer3 = RepeatableTimer(10 - (Inverse_p - Inverse_t), StopServo)
        print(10 - (Inverse_p - Inverse_t))
        Inverse_t = time.time()
        timer_started = False
        timer3.start()
        timer3_started = True
    
    if(name == "Wait5Sec_I" and timer_started == False):
        timer.start()
        timer_started = True
        In_I_Save_State = False
        
    if(name == "Save_I_State" and In_I_Save_State == False):
        Inverse_p = time.time()
        kit.continuous_servo[15].throttle = -0.1111111
        In_I_Save_State = True
    
    if(name != "Operation" and name != "InverseOperation"):
        if pir.motion_detected:
            #i = 1 
             print("Motion detected")
             #led.on()
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
            if(name == "MotionOnly" or name == "MotionOnly_I"):
                print("No motion detected")
                states.on_event('n')
