formatter = "{} {} {} {}"
# 变量formatter的数据类型是字符串
print(type(formatter))
# 取第一行定义的format字符串，调用它的format函数，给format函数传递4个参数，这些参数和formatter变量中的{}匹配
# 在formatter上调用format的结果是一个新字符串，其中的{}被4个变量替换掉了，这就是print('')现在打印出的结果
print(formatter.format(1, 2, 3, 4))
print("{} {} {} {}...".format(4, 3, 2, 1))

print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# demo
poem = "{} {} {} {}"
print(poem.format(
    "老骥伏枥",
    "志在千里",
    "烈士暮年",
    "壮心不已"
))

# demo2
poem = "{} {} {} {}"
print(poem.format(
    'l',
    'o',
    'v',
    'e'
))
#None表示不存在，是一种真正的空，不是空列表，也是不是0或者空字符串
print(None)
# 数据类型是NoneType
print(type(None))
msg = 'hello'
print(msg)
msg = None
print(msg)
print(type(msg))
# unsupported operand type(s) for +: 'int' and 'NoneType'
print(2 + None)
