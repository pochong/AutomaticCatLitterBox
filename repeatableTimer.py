# RepeatableTimer
# Used with the Timer function, but 
# can repeat the timer unlimited time
# since the Timer function can't

from threading import Timer

class RepeatableTimer(object):
    # initialize the RepeatableTimer, paramaters are the same as original Timer function
    def __init__(self, interval, function, args=[], kwargs={}):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        
        self.timer = None
    
    # start is the same as the original Timer function
    def start(self):
        self.timer = Timer(self.interval, self.function, *self.args, **self.kwargs)
        self.timer.start()
    
    # cancel is the same as the original Timer function
    def cancel(self):
        self.timer.cancel()
        