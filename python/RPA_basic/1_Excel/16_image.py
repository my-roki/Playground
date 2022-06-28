from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("lenagray.png")

ws.add_image(img, "C3")

wb.save("image.xlsx")