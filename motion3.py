from gpiozero import MotionSensor
from gpiozero import LED
import time


pir = MotionSensor(21)
led = LED(17)

led.off()
while True:
     if pir.motion_detected:
         print("Motion detected")
         led.on()
         time.sleep(1)
     else:
         print("No Motion")
         led.off()