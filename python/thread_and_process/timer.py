import time

class Timer():
    def __init__(self):
        self.start_time = time.time()
        self.end_time = None

    def end(self):
        self.end_time = time.time()
        print(f"time spent {self.end_time - self.start_time}")