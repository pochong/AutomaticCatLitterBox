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
p = 10
timer2 = Timer(p - t, StopServo)
states = StateMachine()
timer_started = False
timer2_started = False
timer = RepeatableTimer(5, nextState)
kit = ServoKit(channels=16)
prev_rv = 0
int_rv = 0


while True:
    prev_rv = int_rv
    received_data = port.read(4)
    #time.sleep(0.01)
    #data_left = port.inWaiting()
    #received_data += port.read(data_left)
    int_rv = int.from_bytes(received_data,sys.byteorder)
    #print(int_rv/1000000)
    #print((prev_rv/1000000) - (int_rv/1000000))
    if((prev_rv/1000000) - (int_rv/1000000) >= 500):
        print("pressure")
        states.on_event('p')
        if(timer_started == True):
            timer_started = False
            timer.cancel()
        if(timer2_started == True):
            timer2_started = False
            timer_started = False
            timer2.cancel()
        
    name = str(states.state)
    
    if(name == "Initial"):
        timer_started = False
        timer2_started = False
        t = 0
        p = 10
    
    if(name == "Wait5Sec" and timer_started == False):
        timer.start()
        timer_started = True
        
    if(name == "StartOperation" and timer2_started == False):
        kit.continuous_servo[15].throttle = 0.5
        t = time.time()
        timer2.start()
        timer2_started = True
    
    if(name == "SaveState" and timer_started == False):        
        p = time.time()
        timer.start()
        timer_started = True
    
    if(name == "ResumeOperation" and timer2_started == False):
        kit.continuous_servo[15].throttle = 0.5
        t = time.time()
        timer2.start()
        timer2_started = True
        
    
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
             timer2.cancel()
            