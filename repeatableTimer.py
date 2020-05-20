from threading import Timer

class RepeatableTimer(object):
    def __init__(self, interval, function, args=[], kwargs={}):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        
        self.timer = None
        
    def start(self):
        self.timer = Timer(self.interval, self.function, *self.args, **self.kwargs)
        self.timer.start()
        
    def cancel(self):
        self.timer.cancel()
        