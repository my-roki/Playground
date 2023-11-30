import time

from timer import Timer
from threading import Thread

def work(worker_name: str):
    print(f"the {worker_name} starts")
    for i in range(1, 6):
        print(f"{worker_name} is running {i}")
        time.sleep(0.1)
    print(f"the {worker_name} ends")


if __name__ == "__main__":
    td1 = Thread(target=work, args=("worker_01",))
    td2 = Thread(target=work, args=("worker_02",))
    td3 = Thread(target=work, args=("worker_03",))

    timer = Timer()

    td1.start()
    td2.start()
    td3.start()

    # join 함수는 thread가 종료될 때까지 기다립니다.
    td1.join()
    td2.join()
    td3.join()

    timer.end()
