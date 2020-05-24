# state
# This is the declaration of what each state needs to have

class State(object):

    # when initializing the state, print out the state that it is in
    def __init__(self):
        print('processing current state:', str(self))

    # let my_states.py write what happens when an event happens
    def on_event(self, event): 
        pass
    
    # get the name of the state the state machine is in
    def __repr__(self):
        return self.__str__()

    # get the name of the state the state machine is in
    def __str__(self):
        return self.__class__.__name__
    