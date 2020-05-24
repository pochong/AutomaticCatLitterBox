# my_states
# This is the declaration of all the different states of the 
# state machine. Include the state of where to go next
# depending on the inputs of the sensors

# 'p' stands for cat on the pressure sensor, creating a change in pressure
# 'o' stands for the cat leaving the pressure sensor, creating a change in pressure
# 't' stands for the timer is up
# 'm' stands detected motion in PIR motion sensor
# 'n' stands for no motion detected in PIR motion sensor

from state import State

class Initial(State):

    def on_event(self, event):
        if(event == 'p'):
            return PressureON()
        else:
            print("still in Initial")
            return self

class PressureON(State):
    def on_event(self, event):
        if(event == 'o'):
            return Wait5Sec()
        else:
            print("still in PressureON")
            return self

class Wait5Sec(State):
    def on_event(self, event):
        if(event == 'p'):
            return PressureON()
        elif(event == 't'):
            return Operation()
        elif(event == 'm'):
            return MotionOnly()
        else:
            print("Still in Wait5Sec")
            return self
        
class MotionOnly(State):
    def on_event(self, event):
        if(event == 'n'):
            return Wait5Sec()
        elif(event == 'p'):
            return PressureON()
        else:
            print("Still in MotionOnly")
            return self

class Operation(State):
    def on_event(self, event):
        if(event == 'p' or event == 'm'):
            return SaveState()
        elif(event == 't'):
            return Wait5Sec_I()
        else:
            print("Still in Operation")
            return self

class SaveState(State):
     def on_event(self, event):
        if(event == 'p' or event == 'm'):
            print("still in SaveState")
            return self
        elif(event == 'o'):
            return Wait5Sec()
        else:
            print("still in SaveState")
            return self

class Save_I_State(State):
     def on_event(self, event):
        if(event == 'p' or event == 'm'):
            print("still in Save_I_State")
            return self
        elif(event == 'o'):
            return Wait5Sec_I()
        else:
            print("still in Save_I_State")
            return self

class InverseOperation(State):
     def on_event(self, event):
        if(event == 'p' or event == 'm'):
            return Save_I_State()
        elif(event == 't'):
            return Initial()
        else:
            print("Still in InverseOperation")
            return self
        
class Wait5Sec_I(State):
    def on_event(self, event):
        if(event == 'p'):
            return Pressure_I_ON()
        elif(event == 't'):
            return InverseOperation()
        elif(event == 'm'):
            return MotionOnly_I()
        else:
            print("Still in Wait5Sec_I")
            return self

class MotionOnly_I(State):
    def on_event(self, event):
        if(event == 'n'):
            return Wait5Sec_I()
        elif(event == 'p'):
            return Pressure_I_ON()
        else:
            print("Still in MotionOnly_I")
            return self       

class Pressure_I_ON(State):
    def on_event(self, event):
        if(event == 'o'):
            return Wait5Sec_I()
        else:
            print("still in Pressure_I_ON")
            return self