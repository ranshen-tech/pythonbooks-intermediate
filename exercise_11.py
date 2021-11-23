# 在每一个行后面加了end=' ',告诉print不要用换行符结束这一行跑到下一行去
print("How old are you? ", end=' ')
# input负责把后面括号内的内容显示到终端,什么数据都行(True, False, None)
age = input()
print("How tall are you? ", end=' ')
height = input()
print("How much do you weigh? ", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# 查看令我有些疑惑的数据类型
# 都是字符串类型
print(type(age))
print(type(height))
print(type(weight))

# 测试网上搜到的input的例子
# put() 函数接受一个标准输入数据，返回为 string 类型,函数语法：input([prompt])
question_1 = input("What language is your favourite? ")
question_2 = input("What is your name? ")
print(f"My favourite language is {question_1}.")
print("I'm {}.".format(question_2))

# 如何读取用户输入的数并进行数学运算
# 从input()获取字符串形式的数值，然后用int()把它转化为整数
# x = int(input())
