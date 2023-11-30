from timer import Timer
from threading import Thread


def calculate(id, start, end):
    total = 0
    print(f"Thread {id} starts")
    for i in range(start, end):
        total += i
    print(f"Thread {id} ends")
    return


if __name__ == "__main__":
    START, END = 0, 100000000
    
    th1 = Thread(target=calculate, args=(1, START, END))
    th2 = Thread(target=calculate, args=(2, START, END))

    timer = Timer()

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    timer.end()
