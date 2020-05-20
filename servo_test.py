from adafruit_servokit import ServoKit
import time

#kit = MotorKit()
#pwm = PWM(0x40)
#pwm.set_pwm_freq(100)
#pwm.set_pwm(15, 1024,3072)
kit = ServoKit(channels=16)
#while(1):
    #kit.continuous_servo[15].throttle = 1
    #print("in 1 throttle")
    #time.sleep(10)
    #kit.continuous_servo[15].throttle = 0
    #print("in 0 throttle")
    #time.sleep(20)
    #kit.continuous_servo[0].throttle = -1
  
#kit.servo[0].actuation_range = 180

#kit.servo[11].angle = 90
#kit.servo[12].angle = 180
#time.sleep(1)
kit.continuous_servo[15].throttle = 0.5
#kit.continuous_servo[8].throttle = 1
t = time.time()
#print(t)
time.sleep(4)
#kit.continuous_servo[15].throttle = -0.5
#kit.continuous_servo[8].throttle = -1
#time.sleep(2)
#kit.servo[11].angle = 0
#kit.servo[12].angle = 0
#kit.continuous_servo[15].throttle = 0
#time.sleep(2)
p = time.time()
print(p-t)
kit.continuous_servo[15].throttle = -0.1111111
#kit.continuous_servo[8].throttle = 0
#time.sleep(0.1)