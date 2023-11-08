import time

class Timer:
    def __init__(self, the_time):
        self.the_time = the_time
        self.given_time = the_time
    
    def get_time(self):
        return self.given_time
    
    def start(self):
        while self.given_time > 0:
            print(self.given_time)
            time.sleep(1)
            self.given_time -= 1
    
    def reset(self):
        self.given_time = self.the_time

timer = Timer(10)
timer.start()