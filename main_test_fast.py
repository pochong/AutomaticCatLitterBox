# main_test_fast
# This is used to shorten the time to run lots of test
# also put in random timers to see if something unexpected happens
# Testing to see the robustness of the state machine, see if there is a state that 
# breaks the code in one way or another

# The place where the random.randint(500000,1000000) can also be changed 
# to change the probability of the input getting through the timer

from state_machine import StateMachine
from func_timeout import *
import random
import time

states = StateMachine()

timer = time.time




def random_state():
    number = random.randint(0,4)
    if(number == 0):
        while 1:
            time.time()
    elif (number == 1):
        for x in range (random.randint(100000,500000)):
            i = 0
        print("in p")
        states.on_event('p')
        return
    elif (number == 2):
        for x in range (random.randint(100000,500000)):
            i = 0
        print("in n")
        states.on_event('n')
        return
    elif (number == 3):
        for x in range (random.randint(100000,500000)):
            i = 0
        print("in m")
        states.on_event('m')
        return
    elif (number == 4):
        for x in range (random.randint(100000,500000)):
            i = 0
        print("in o")
        states.on_event('o')
        return
    else:
        return


count = 0
# loop it 50 times
for x in range(50) :
    try:
        #set up timer for 0.006000 seconds, if time up run except part of the code
        func_timeout(0.006000, random_state)
    except FunctionTimedOut:
        print("Time Up")
        count = count + 1
        states.on_event('t')

print(count)
