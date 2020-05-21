from threading import Timer
from repeatableTimer import RepeatableTimer
import time

def nextState():
    print("This works")
    #print(time_started)
    timer_started = False
    #print(time_started)
    
#timer = Timer(5, nextState)
timer_started = False
print("Start")
name = 10
timer = RepeatableTimer(name, nextState)
timer.start()
print("Starting")
time.sleep(5)
print("cancel")
timer.cancel()
name = 4
print("change duration")
timer = RepeatableTimer(name, nextState)
print("starting2")
timer.start()
time.sleep(10)
print("cancel2")
timer.cancel()
#while True:
#    name = name + 1
#    #print(name)
#    if(name == 1):
#        print("Starting Timer")
#        timer.start()
#        timer_started = True
#        
#    if(name == 1000000 and timer_started == False):
#        print("Starting Timer2")
#        timer.start()
#        timer_started = True
#        
#    if(name == 2000000):
#        print("Cancelling timer")
#        timer.cancel()
#        timer_started = False
#        
#    if(name == 5000000 and timer_started == False):
#        print("starting timer3")
#        timer.start()
#        timer_started = True
#        
#    print(timer_started)
#        
        