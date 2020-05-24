# state_machine
# This is the declartion of the state machine.

from my_states import Initial

class StateMachine(object):

    # for initializing the state machine
    def __init__(self):
        self.state = Initial()

    # move onto the next state of the state machine depending on the event
    def on_event(self, event):
        self.state = self.state.on_event(event)

