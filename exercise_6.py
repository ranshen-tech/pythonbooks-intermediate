# 把整数10赋值给变量types_of_people
types_of_people =10
# 将变量types_of_people放进另一个字符串，同时将这个字符串赋值给变量x
x =f"There are {types_of_people} types of people."

# 将字符串"binary"赋值给变量binary
binary ="binary"
# 将字符串"don't"赋值给变量do_not
do_not ="don't"
# 将被字符串赋值的变量binary和do_not放进另一个字符串，并将这个字符串赋值给y
y =f"Those who know {binary} and those who {do_not}."

# 打印变量x
print(x)
# 打印变量y
print(y)

# 将被字符串赋值的变量x放进另一个字符串，并将整句打印
print(f"I said: {x}")
# 将被字符串赋值的变量y放进另一个字符串，并将整句打印
print(f"I also said: '{y}'")

# 将False赋值给变量hilarious
hilarious =False
# 将字符串"Isn't that joke so funny? ! {}"赋值给变量joke_evaluation
joke_evaluation ="Isn't that joke so funny? ! {}"
# 将变量hilarious用格式化语法.format()放进另一个被赋值的变量joke_evaluation，并打印整句
print(joke_evaluation.format(hilarious))

# 将字符串赋值给变量w
w ="This is the left side of..."
# 将另一串字符串赋值给变量e
e ="a string with a right side."

# 将被字符串赋值后的两个变量w和e相加，并打印
print(w +e)

# 仿照24，26，28句做的小尝试
demo =True
msg ="Is it {}?"
print(msg.format(demo))

# 查看上文中令我有些疑惑的数据类型
print(type(x))
print(type(y))
print(type(hilarious))
print(type(joke_evaluation))
print(type(demo))
print(type(msg))
print(type(joke_evaluation.format(hilarious)))
print(type(msg.format(demo)))
