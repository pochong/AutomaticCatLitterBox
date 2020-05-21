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

class StartTimer(State):
    def on_event(self, event):
        return Wait5Sec()

class Wait5Sec(State):
    def on_event(self, event):
        if(event == 'p' or event == 'm'):
            return PressureON()
        elif(event == 't'):
            return Operation()
        else:
            print("Still in Wait5Sec")
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
        if(event == 'p' or event == 'm'):
            return Pressure_I_ON()
        elif(event == 't'):
            return InverseOperation()
        else:
            print("Still in Wait5Sec_I")
            return self
        
class Pressure_I_ON(State):
    def on_event(self, event):
        if(event == 'o'):
            return Wait5Sec_I()
        else:
            print("still in Pressure_I_ON")
            return self