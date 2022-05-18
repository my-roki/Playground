import time


def delivery(name, mealtime):
    print(f"{name}에게 배달을 완료하였습니다.")
    time.sleep(mealtime)
    print(f"{name} 식사 완료, 식사시간 : {mealtime} 시간..")
    print(f"{name} 그릇 수거 완료!")
    print()


def main():
    delivery("A", 3)
    delivery("B", 2)
    delivery("C", 1)


if __name__ == "__main__":
    start = time.time()
    print(main())  # None
    end = time.time()
    print(end - start)
