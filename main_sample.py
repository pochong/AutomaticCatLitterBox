from gpiozero import MotionSensor
from gpiozero import LED
from state_machine import StateMachine
from func_timeout import *
import time

pir = MotionSensor(4)
led = LED(17)

states = StateMachine()

led.off()
while True:
     if pir.motion_detected:
         print("Motion detected")
         led.on()
         states.on_event('m')
         time.sleep(7)
     else:
         print("No Motion")
         led.off() 