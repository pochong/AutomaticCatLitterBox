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
        if(event == 'p'):
            return Wait5Sec()
        else:
            print("still in PressureON")
            return self

class StartTimer(State):
    def on_event(self, event):
        return Wait5Sec()

class Wait5Sec(State):
    def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            return PressureON()
        elif(event == 't'):
            return StartOperation()
        else:
            print("Still in Wait5Sec")
            return self

class StartOperation(State):
    def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            return SaveState()
        elif(event == 't'):
            return Initial()
        else:
            print("Still in StartOperation")
            return self

class SaveState(State):
     def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            print("still in SaveState")
            return self
        elif(event == 't'):
            return ResumeOperation()
        else:
            print("still in SaveState")
            return self

class ResumeOperation(State):
     def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            return SaveState()
        elif(event == 't'):
            return Initial()
        else:
            print("Still in ResumeOperation")
            return self