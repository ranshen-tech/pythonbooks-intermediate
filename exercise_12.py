# 用input重写exercise_11.py
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# 终端pydoc命令
# python自带的文档生成工具，查看类和方法结构
# 格式：
# pydoc open
# pydoc file

# 可以，但input()的结果没有存到变量中
print("How old are you?", input())
