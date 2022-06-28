import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
from tkinter import filedialog
from PIL import Image  


# 파일 추가
def add_file(list_file):
    files = filedialog.askopenfilenames(
        title="이미지 파일을 선택하세요", 
        filetypes=(("PNG파일", "*.png"), ("모든 파일", "*.*")),
        initialdir=r"C:")  # 최초 탐색 경로
    
    for file in files: 
        # print(file)
        list_file.insert(END, file)


# 파일 삭제
def delete_file(list_file):
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# 저장 경로 설정(폴더)
def browse_dest_path(txt_dst_path):
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':  # 사용자가 취소를 누를 때
        return       
    txt_dst_path.delete(0, END)
    txt_dst_path.insert(0, folder_selected)


# 이미지들을 merge
def merge_image(cmb_width,cmb_space,cmb_format,list_file,txt_dst_path,p_var,progress_bar): 
    try:
        # 가로넓이
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1
        else:
            img_width = int(img_width)
        
        # 간격
        img_space = cmb_space.get()
        if img_space == "없음":
            img_space = 0
        elif img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90

        # 포맷
        img_format = cmb_format.get().lower()

        # print(list_file.get(0,END))
        images = [Image.open(i) for i in list_file.get(0,END)]
        image_sizes = []

        """
        원본 width : 원본 height = 변경 width : 변경 height

        원본 height * 변경 width = 원본 width * 변경 height
        변경 height = (원본 height * 변경 width)/원본 width
        """ 
        if img_width > -1:
            image_sizes = [(int(img_width), int((i.size[1] * img_width)/i.size[0])) for i in images]
        else:
            image_sizes = [(i.size[0], i.size[1]) for i in images]

        widths, heights = zip(*(image_sizes))
        # widths = [i.size[0] for i in images]
        # heights = [i.size[1] for i in images]
        # print("width: ", widths)
        # print("height: ", heights)

        # 이미지들을 merge
        max_width, total_height = max(widths), sum(heights)
        # print(max_width)
        # print(total_height)

        if img_space > 0 :
            total_height += (img_space * (len(images)-1))

        result_image = Image.new("RGB", (max_width, total_height), (255,255,255))
        
        y_offset = 0 # y위치 정보
        for idx, img in enumerate(images):
            # width가 원본 유지가 아닐 때는 이미지 크기 조정해야 함
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_image.paste(img, (0,y_offset))
            y_offset += (img.size[1] + img_space)  # height값 + 사용자가 정한 간격

            progress = ((idx + 1) / len(images)) *  100  # percentage
            p_var.set(progress)
            progress_bar.update() 

        dst_path = os.path.join(txt_dst_path.get(), f"merged_image.{img_format}")
        result_image.save(dst_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as e:
        msgbox.showerror("error", e)


def start(cmb_width, cmb_space, cmb_format, list_file, txt_dst_path, p_var, progress_bar):
    # 각 옵션 확인
    # print("가로넓이:", cmb_width.get())
    # print("간격:", cmb_space.get())
    # print("포맷:", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
        return
    
    # 저장경로 확인
    if len(txt_dst_path.get()) == 0:
        msgbox.showwarning("경고", "저장경로를 선택하세요.")
        return  
    
    # 이미지 통합 작업
    merge_image(cmb_width, cmb_space, cmb_format, list_file, txt_dst_path, p_var, progress_bar)


