#%%
# 파일 기본
import os
print(os.getcwd())  # current working directory 현재 작업 공간

os.chdir("RPA_basic")   # change directory, RPA_basic으로 이동
print(os.getcwd())

os.chdir("..")  # 상위 경로로 이동
print(os.getcwd())

os.chdir("../..")   # 상위의 상위 폴더로 이동
print(os.getcwd())

os.chdir("c:/") # 주어진 절대 경로로 이동
print(os.getcwd())


#%%
# 파일 경로
file_path = os.path.join(os.getcwd(), "my_file.txt")
print(file_path)

# 파일 경로에서 폴더 정보 가져오기
print(os.path.dirname(r"D:\workpractice\mylogfile_20210310113328.log"))

# 파일 정보 가져오기
import time
import datetime

# 파일의 생성날짜
ctime = os.path.getctime(r"D:\workpractice\RPA_basic\1_excel\1_create_file.py")
print(ctime)
print(datetime.datetime.fromtimestamp(ctime))
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))   # 날짜 정보를 strftime 을 통해서 년월일 시분초 형태로 출력

# 파일의 수정날짜
mtime = os.path.getmtime(r"D:\workpractice\RPA_basic\1_excel\1_create_file.py")
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))  

# 파일의 마지막 접근 날짜
atime = os.path.getatime(r"D:\workpractice\RPA_basic\1_excel\1_create_file.py")
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S")) 

# 파일 크기
size = os.path.getsize(r"D:\workpractice\RPA_basic\1_excel\1_create_file.py")
print(size, "byte")  # 파일 사이즈는 바이트 단위로 출력


#%%
import os

# 파일 목록 가져오기
print(os.listdir())
print(os.listdir(r"D:\workpractice\RPA_basic"))

# %%
# 파일 목록 가져오기(하위 폴더 포함)
result = os.walk(r"D:\workpractice\RPA_basic")
print(result)

for root, dirs, files in result:
    print(root, dirs, files)

# %%
# 만약 폴더 내에서 특정 파일들을 찾으려면?
name = "11_file_system.py"
result = []
for root, dirs, files in os.walk("."):
    if name in files:
        result.append(os.path.join(root,name))
print(result)


# %%
# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면? ex)*.xlsx, *txt ...
import fnmatch
pattern = "*.py"
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
           result.append(os.path.join(root, name))
print(result)


#%%
# 주어진 경로가 파일인지 폴더인지 알아보자
print(os.path.isdir("../../RPA_basic"))   # rpa_basic 은 폴더인가? True
print(os.path.isfile("../../RPA_basic"))  # rpa_basic 은 파일인가? False

# 만약에 지정된 경로에 해당하는 파일 또는 폴더가 없다면? False
print(os.path.isdir("nothing"))   
print(os.path.isfile("nothing")) 

# 주어진 경로가 존재하는 지 여부
if os.path.exists("mylogfile_20210310113328.log"):
    print("directory exsist")
else:
    print("directory doesn't exsist")


#%%
# 파일 만들기
open("new_file.json", "a").close() # 빈 파일 생성

# 파일명 변경하기
os.rename("new_file.json", "new_file.xml")

# 파일 삭제하기
os.remove("new_file.xml")


#%%
# 폴더 만들기
os.mkdir("new_folder")  # 현재 경로 기준으로 폴더 생성
os.mkdir(r"D:\workpractice\new_folder") # 절대 경로 기준으로 폴더 생성


#%%
# os.mkdir("new_folders/a/b/c/")  # 실패 : 하위 폴더를 가지는 폴더 생성 시도
os.makedirs("new_folders/a/b/c/")  # 성공 : 하위 폴더를 가지는 폴더 생성


#%%
# 폴더명 변경하기
os.rename("new_folder", "new_folder_rename")


#%%
# 폴더 지우기
# os.rmdir(r"RPA_basic\2_Desktop\new_folder_rename")
os.rmdir("new_folders")    # 폴더 안이 비었을 때만 삭제 가능


#%%
import shutil
shutil.rmtree("new_folders")    # 폴더 안이 비어있지 않아도 완전 삭제 가능
    # 모든 파일이 삭제될 수 있으므로 주의!!!!!!!


#%%
# 파일 복사하기
    # 어떤 파일을 폴더 안으로 복사하기
shutil.copy(r"new_file.json", r"new_folder")    # 원본파일 경로, 대상 폴더 경로 
shutil.copy(r"new_file.json", r"new_folder\new_file_copy.json") # 원본 파일 경로, 대상 경로(변경된 파일 명) 
shutil.copyfile(r"new_file.json", r"new_folder\new_file_copy2.json")  # 원본 파일 경로, 대상 파일 경로. 폴더 경로까지만 쓰면 error


#%%
shutil.copy(r"new_file.json", r"new_folder\new_file_copymetainfonot.json")
shutil.copy2(r"new_file.json", r"new_folder\new_file_copymetainfo.json") # 원본 파일 경로, 대상 경로(변경된 파일 명) 

# copy 또는 copyfile : 메타정보를 복사 x
# copy2 : 메타정보를 복사 o


#%%
# 폴더복사
shutil.copytree("new_folder", "new_folder_copy_with_file")  # 원본 폴더 경로, 대상 폴더 경로(하위 폴더 모두 복사)


#%%
# 폴더 이동
# shutil.move("new_folder_copy_with_file", "new_folder")   # 이동하고 싶은 폴더 경로, 이동 할 폴더 경로
shutil.move("new_folder", "new_folder_rename")  # 폴더명 변경되는 효과
