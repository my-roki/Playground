print("Hello World")

from openpyxl import Workbook

wb = Workbook() #새 워크북 생성
ws = wb.active # 현재 활성화 된 sheet 가져옴
ws.title = "testworks" # sheet의 이름을 변경
wb.save("create_file.xlsx")
wb.close()


