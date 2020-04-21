from state import State



class Initial(State):

    def on_event(self, event):
        if(event == 'p'):
            return PressureON()

        return self

class PressureON(State):
    def on_event(self, event):
        if(event == 'o'):
            return StartTimer()

        return self

class StartTimer(State):
    def on_event(self, event):
        return Wait5Sec()

class Wait5Sec(State):
    def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            return PressureON()
        else:
            return StartOperation()

class StartOperation(State):
    def on_event(self, event):
        if(event == 'p' or event == 'm' or event == 'n'):
            return SaveState()
        else:
            return Initial()

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