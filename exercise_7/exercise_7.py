# 加注释只是为了解释难懂的代码，或者注明为什么要这么写代码（重要）
print("Mary had a little lamb.")
# format方法添加一个内容为单词snow的字符串，变量名是不会带引号的
print("Its fleece was white as {}.".format('snow'))
# 变量可以是整数、浮点数、字符串
name = True
print("My name is {}.".format(name))
# 数据类型是字符串
print(type("My name is {}.".format(name)))
print("And everywhere that Mary went.")
# 将字符串乘10，并打印
print("." * 10) # what'd that do?

# 单引号一般用来创建简短的字符串，如'a'，‘snow'
end1 ="C"
end2 ="h"
end3 ="e"
end4 ="e"
end5 ="s"
end6 ="e"
end7 ="B"
end8 ="u"
end9 ="r"
end10 ="g"
end11 ="e"
end12 ="r"

# watch that comma at the end. try removing it to see what happends
# end是防止换行，数据类型是字符串或者None,可以把下一行和本行end后面的字符串连接起来
print(end1 +end2 +end3 +end4 +end5 +end6, end=' ')
print(end7 +end8 +end9 +end10 +end11 +end12)

a = 'ran'
b = 'shen'
print(a.title(), end=' ')
print(b.title())
print(end1)
print(end2)
print(end3, end=' ')
print(end4)
print(end5, end='')
print(end6)
