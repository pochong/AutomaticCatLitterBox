from my_states import Initial

class StateMachine(object):

    def __init__(self):
        self.state = Initial()

    def on_event(self, event):
        self.state = self.state.on_event(event)

