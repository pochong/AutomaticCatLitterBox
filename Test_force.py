# Test_force
# used for testing the different ways of getting the signals of the force sensor

import serial
import sys
from time import sleep

port = serial.Serial("/dev/ttyAMA0", 115200)
prev_rv = 0
int_rv =0

while True:
    #print("working")
    prev_rv = int_rv
    #sleep(0.01)
    #data_left = port.inWaiting()
    #received_data += port.read(data_left)
    p = 0
    for x in range(50):
        received_data = port.read(4)
        p += int.from_bytes(received_data,sys.byteorder)
    int_rv = p
    print(int_rv/1000000)
    #print((prev_rv/1000000) - (int_rv/1000000))
    if((prev_rv/1000000) - (int_rv/1000000) >= 10000 or (int_rv/1000000) - (prev_rv/1000000) >= 10000):
        print("change in pressure")
        
        
        
        