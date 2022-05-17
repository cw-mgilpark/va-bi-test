import os
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

#files 변수에 선택 파일 경로 넣기
files = filedialog.askopenfilenames(initialdir="/",\
                 title = "파일을 선택 해 주세요",\
                    filetypes = (("*.xlsx","*xlsx"),("*.xls","*xls"),("*.csv","*csv")))

#파일 선택 안했을 때 메세지 출력
if files == '':
    messagebox.showwarning("경고", "파일을 추가 하세요")

print(files)    #files 리스트 값 출력

#dir_path에 파일경로 하나씩 넣어서 읽기
for dir_path in files:
    df = pd.read_excel(dir_path, header= 0 , usecols='A, C, D, E')   #엑셀 파일의 C, G, I 열만 읽기

A_list = []     # A열을 C_list에 생성
C_list = []     # C열을 C_list에 생성
D_list = []     # D열을 C_list에 생성
E_list = []     # E열을 C_list에 생성

for i in df.values:
    A_list.append(i[0])		# C열을 C_list에 저장
    C_list.append(i[1])		# G열을 G_list에 저장
    D_list.append(i[2])		# I열을 I_list에 저장
    E_list.append(i[3])  # I열을 I_list에 저장

print(len(A_list))
print(C_list)
print(D_list)
print(E_list)