# 另一种将变量传递给脚本的方法
# 脚本就是你编写的.py程序

# argv即所谓的参数变量（argument variable）
from sys import argv
# read the WYSS section for how to run this
# 将argv解包（unpack），将其赋值给4个变量
script, first, second, third = argv

# 需要在终端输入命令：python3 exercise_13/exercise_13.py 1 2 3
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


consolidation_exercise_1
from sys import argv
script, name, age = argv

print("This script is called:", script)
print("My name is:",name)
print("I'm {age} years old.")


# consolidation_exercise_2
from sys import argv
script, name, age, height, weight = argv

print("This script is called:", script)
print("My name is:", name)
print("I'm {age} years old.")
print("My height is:", height)
print("My weight is:", weight)


# consolidation_exercise_3 将input和argv一起用，让脚本从用户那边得到更多的输入
# 不要想多了，只是用argv得到一些东西，用input从用户那里得到另外一些东西。
from sys import argv
script, first, second, third = argv

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

name = input("What's your name? ")
age = input("How old are you? ")

print(f"My name is {name}, I'm {age} years old.")
