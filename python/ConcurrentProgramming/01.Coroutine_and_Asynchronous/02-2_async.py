import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달을 완료하였습니다.")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, 식사시간 : {mealtime} 시간..")
    print(f"{name} 그릇 수거 완료!")
    print()


async def main():
    await asyncio.gather(
        delivery("A", 3),
        delivery("B", 2),
        delivery("C", 1),
    )


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
