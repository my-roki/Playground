# https://docs.python.org/3.7/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session, url = params[0], params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com"] * 10

    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
    # max_workers=1 -> 3.880382537841797
    # max_workers=10 -> 0.8039553165435791
