import time
import random
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def alert_for_me(message):
    pass


def list_chuck(arr, n):
    return [arr[round(len(arr) * i / n) : round(len(arr) * (i + 1) / n)] for i in range(0, n)]


def check_seat(driver, seats):
    print(driver, seats)
    for seat in seats:
        is_available = seat.get_attribute("fill")
        if is_available == "none":
            continue
        elif is_available == "#DDDDDD":
            continue
        else:
            print("gotcha!")
            seat.click()
            for _ in range(20):
                try:
                    submit = driver.find_element(By.ID, "nextTicketSelection")
                    submit.click()
                except:
                    continue
            return False
    return True


def main():
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver")
    driver.get("https://ticket.melon.com/main/index.html")

    time.sleep(60)  # login in this time

    wait = WebDriverWait(driver, 1000000)
    try:
        # NetFunnel_Skin_Top
        print(datetime.now(), "Waiting...")
        wait.until_not(EC.presence_of_element_located((By.ID, "NetFunnel_Skin_Top")))
    except selenium.common.exceptions.TimeoutException:
        raise Exception("Timed out!")
    finally:
        print(datetime.now(), "Opened! Write Secret Code, activate seats!")
        time.sleep(30)

    driver.switch_to.window(driver.window_handles[-1])
    print(datetime.now(), "Connecting", driver.current_url)

    driver.switch_to.frame("oneStopFrame")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "divGradeSummary")))
    s_section_list = driver.find_element(By.XPATH, '//*[@id="divGradeSummary"]/tr[6]/td/div/ul')

    not_catch = True
    while not_catch:
        for s_section_button in s_section_list.find_elements(By.TAG_NAME, "li"):
            # irregular click
            rand_interval = random.uniform(0.5, 1.2)
            # time.sleep(rand_interval)

            s_section_button.click()
            print(datetime.now(), s_section_button.text)

            # "#ez_canvas > svg"
            # '//*[@id="ez_canvas"]/svg'
            s_section_seats = driver.find_element(By.CSS_SELECTOR, "#ez_canvas > svg")
            s_seats = s_section_seats.find_elements(By.TAG_NAME, "rect")
            s_seats_split = list_chuck(s_seats, 10)

            executor = ProcessPoolExecutor(max_workers=10)
            result = executor.map(check_seat, [driver] * len(s_seats_split), s_seats_split)
            print(result)
            executor.shutdown(wait=True)


if __name__ == "__main__":
    main()
