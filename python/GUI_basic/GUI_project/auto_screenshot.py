from PIL import ImageGrab
import time
import keyboard

"""
F9 번을 누르면 스크린 샷
찍힌 이미지는 screenshot_현재시간.png 으로 저장
esc 키를 누르면 프로그램 종료
"""

# time.sleep(5) # 5초 대기 : 사용자가 준비하는 시간

# for i in range(1,11):
#     img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
#     img.save(f"image{i}.png")
#     time.sleep(2)  # 2초 쉼

def screenshot():
    img = ImageGrab.grab()
    img.save(f"screenshot_{time.strftime('%Y%m%d%H%M%S')}.png")

keyboard.add_hotkey("F9", screenshot)
keyboard.wait("esc")  # 사용자가 esc를 누를 때까지 프로그램 수행