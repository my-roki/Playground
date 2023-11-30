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

    # 총 연산을 두개의 스레드로 나눠서 처리합니다.
    th1 = Thread(target=calculate, args=(1, START, END // 2))
    th2 = Thread(target=calculate, args=(2, END // 2, END))

    timer = Timer()

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    timer.end()
