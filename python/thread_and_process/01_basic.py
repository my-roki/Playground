import time

from timer import Timer


def work(worker_name: str):
    print(f"the {worker_name} starts")
    for i in range(1, 6):
        print(f"{worker_name} is running {i}")
        time.sleep(0.1)
    print(f"the {worker_name} ends")


if __name__ == "__main__":
    timer = Timer()

    work("worker_01")
    work("worker_02")
    work("worker_03")

    timer.end()
