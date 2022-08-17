# -*- coding:utf-8 -*-

import re,sys,os,time
import PyPDF2

print("请在工具目录下创建res文件夹，拖入相关文件到此文件夹！")
#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def returnXieGang(path):
    som = "\\"
    some = r"\\"
    return path.replace(som,some)

a = input("输入你要解压的文件名（含后缀）：")
l = ["Python_TricksAlluwant.pdf"]
l.append(a)
print(f"列表有：{l}")
# 生成待破解文件的目录
if l[1] == "":
    print("您未输入要破解的文件，所以将按照默认文件进行破解！(huzk制作)")
    a = l[0]
    filePDF = resource_path(os.path.join("res", "Python_TricksAlluwant.pdf"))
else:
    a = l[1]
    filePDF = resource_path(os.path.join("res", a))
filePDF = returnXieGang(filePDF)
print(filePDF)
print("请耐心等待，需要些时间。。。")


#访问res文件夹下数据.txt的内容
filename = resource_path(os.path.join("res","mydic.txt"))
filename = returnXieGang(filename)
print(filename)
# ————————————————


with open(filePDF, 'rb') as pdf_file_stream:
    reader = PyPDF2.PdfFileReader(pdf_file_stream)
    with open(filename, 'r') as txt_file_stream:
        file_iter = iter(lambda: txt_file_stream.readline(), '')
        for word in file_iter:
            word = re.sub(r'\s', '', word)
            if reader.decrypt(word):
                print(f"请提取密码：{word}")
                time.sleep(5)
                break
