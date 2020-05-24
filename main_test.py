# main_test
# This is testing whether the state machine works as intended by
# getting user inputs to substitute sensor input

from state_machine import StateMachine
from func_timeout import *
import time

states = StateMachine()
timer = time.time()

#used for substituting the time waiting part of the state machine
def Timer():
    events = input()
    return events

while 1:
    event = input()
    states.on_event(event)
    #print(states.state)
    #print(name)
    name = str(states.state)
    #print(name == 'Wait5Sec' or name  == "Wait5Sec_I")
    if(name == 'Wait5Sec'):
        try:
            events = func_timeout(5, Timer)
            states.on_event(events)
        except FunctionTimedOut:
            print("Timed Out")
            events = 't'
            states.on_event(events)
    name = str(states.state)
    if(name == 'Operation' or name == 'InverseOperation'):
        try:
            events = func_timeout(10,Timer)
            states.on_event(events)
        except FunctionTimedOut:
            print("Finished")
            events = 't'
            states.on_event(events)
    name = str(states.state)

        
    