from state_machine import StateMachine
from func_timeout import *
import time

states = StateMachine()
timer = time.time()

def Timer():
    events = input()
    return events

while 1:
    event = input()
    ticks = time.time()
    print("time difference: ", ticks - timer)
    states.on_event(event)
    #print(states.state)
    name = str(states.state)
    #print(name)
    print(name == 'StartTimer')
    if(name == 'StartTimer'):
        states.on_event(event)
    name = str(states.state)
    print(name == 'Wait5Sec')
    if(name == 'Wait5Sec'):
        try:
            events = func_timeout(5, Timer)
            states.on_event(events)
        except FunctionTimedOut:
            print("Timed Out")
            events = 'l'
            states.on_event(events)
    name = str(states.state)
    if(name == 'StartOperation' or name == 'ResumeOperation'):
        try:
            events = func_timeout(10,Timer)
            states.on_event(events)
        except FunctionTimedOut:
            print("Finished")
            events = 'l'
            states.on_event(events)
    name = str(states.state)
    if(name == 'SaveState'):
        try:
            events = func_timeout(5,Timer)
            states.on_event(events)
        except FunctionTimedOut:
            print("Out Timed")
            events = 'l'
            states.on_event(events)
    name = str(states.state)
    if(name == 'ResumeOperation'):
        try:
            events = func_timeout(10,Timer)
            states.on_event(events)
        except FunctionTimedOut:
            print("Finished")
            events = 'l'
            states.on_event(events)

        
    