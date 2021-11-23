# 代码1-3行使用argv来获取文件名
from sys import argv

script, filename = argv
# 将获取到的文件打开，并赋值txt变量
txt = open(filename)
# 打印文件名
print(f"Here's your file {filename}:")
# 用read()函数读取文件内容，并打印
print(txt.read())


# 用input输入再次输入文件名
print("Type the filename again:")
# ❗️打开的file要连着文件夹的名字(exercise_15/ex15_sample.txt)
file_again = input('>')
# 将获取到的文件打开，并赋值txt_again变量
txt_again = open(file_again)
# 用read()函数读取文件内容并打印
print(txt_again.read())
