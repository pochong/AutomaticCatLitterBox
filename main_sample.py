from gpiozero import MotionSensor
from gpiozero import LED
from state_machine import StateMachine
#from func_timeout import *
import time
import serial
import sys


port = serial.Serial("/dev/ttyAMA0", 115200)

pir = MotionSensor(21)
#led = LED()

states = StateMachine()
prev_rv = 0
int_rv = 0
#led.off()
while True:
    time.sleep(1)
    prev_rv = int_rv
    received_data = port.read()
    #time.sleep(0.01)
    data_left = port.inWaiting()
    received_data += port.read(data_left)
    int_rv = int.from_bytes(received_data,sys.byteorder)
    #print(int_rv/1000000)
    if(prev_rv - int_rv >= 10000000000000000000):
        print("pressure")
        states.on_event('p')
    else:
        print("no change in pressure")
        states.on_event('o')
    pir.when_motion = states.on_event
    if pir.motion_detected:
         print("Motion detected")
         #led.on()
         #states.on_event('m')
         #time.sleep(7)
    else:
         print("No Motion")
         #led.off() 