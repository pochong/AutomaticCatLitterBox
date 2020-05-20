from state import State



class Initial(State):

    def on_event(self, event):
        if(event == 'p'):
            return PressureON()
        else:
            return self

class PressureON(State):
    def on_event(self, event):
        if(event == 'o'):
            return StartTimer()
        else:
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
            return self

class StartOperation(State):
    def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            return SaveState()
        elif(event == 't'):
            return Initial()
        else:
            return self

class SaveState(State):
     def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            return self
        else:
            return ResumeOperation()

class ResumeOperation(State):
     def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            return SaveState()
        else:
            return Initial()