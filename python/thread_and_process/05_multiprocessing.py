from timer import Timer
from multiprocessing import Process


def calculate(id, start, end):
    total = 0
    print(f"Thread {id} starts")
    for i in range(start, end):
        total += i
    print(f"Thread {id} ends")
    return


if __name__ == "__main__":
    START, END = 0, 100000000
    th1 = Process(target=calculate, args=(1, START, END // 2))
    th2 = Process(target=calculate, args=(2, END // 2, END))

    timer = Timer()

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    timer.end()
