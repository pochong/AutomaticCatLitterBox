from state_machine import StateMachine
from func_timeout import *
import time

states = StateMachine()
timer = time.time()

def Timer():
    while 1:
        time.time()

def GoNextState_p():
    time.sleep(0.002)
    states.on_event('p')

def GoNextState_n():
    time.sleep(0.004)
    states.on_event('n')

def GoNextState_m():
    time.sleep(0.001)
    states.on_event('m')

#ticks = time.time()
#print("time difference: ", ticks - timer)
states.on_event('p')
#name = str(states.state)
states.on_event('o')
states.on_event('m')    #useless input to move to next state
try:                    #Wait5Sec
    func_timeout(0.005,GoNextState_p)
except FunctionTimedOut:
    print("Finished_Wait5Sec")
    states.on_event('p')
states.on_event('p')
states.on_event('o')
states.on_event('n')    #useless input to move to next state
try:                    #Wait5Sec
    func_timeout(0.005,Timer)
except FunctionTimedOut:
    print("Finished_Wait5Sec_2nd")
    states.on_event('d')
try:                    #StartOperation
    func_timeout(0.010,GoNextState_m)
except FunctionTimedOut:
    print("Finished_StartOperation")
    states.on_event('d')
try:                    #SaveState
    func_timeout(0.005,GoNextState_p)
except FunctionTimedOut:
    print("Finished_SaveState")
    states.on_event('d')
try:                    #SaveState
    func_timeout(0.005,Timer)
except FunctionTimedOut:
    print("Finished_SaveState_2nd")
    states.on_event('d')
try:                    #ResumeOperation
    func_timeout(0.007,GoNextState_n)
except FunctionTimedOut:
    print("Finished_ResumeOperation")
    states.on_event('d')
try:                    #SaveState
    func_timeout(0.005,Timer)
except FunctionTimedOut:
    print("Finished")
    states.on_event('d')
try:                    #ResumeOperation
    func_timeout(0.005,Timer)
except FunctionTimedOut:
    print("Finished")
    states.on_event('d')