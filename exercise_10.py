# 转义序列 escape sequence

# 将字符串中的双引号转义("当普通字符打印)
print("I am 6'2\" tall.")

# 将字符串中的单引号转义('当普通字符打印)
print('I am 6\'2" tall.')

# 在一组三引号之间放入任意多行文本

# tabby_cat：虎斑猫
# tab：标签
# 制表符
tabby_cat = "\tI'm tabbed in."
print(tabby_cat)

# persian_cat: 波斯猫
# 换行符
persian_cat = "I'm split\non a line."
print(persian_cat)

# backslash：反斜杠
# 反斜杠符号
backslash_cat = "I'm \\ a \\ cat."
print(backslash_cat)

# 下一行续行符
msg = "i love python, \
because it's beautiful."
print(msg)

# 记住这个格式
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(fat_cat)

# 将转义序列和格式化字符串组合到一起
name = 'ranshen'
message = '''
My {} is ranshen,
I love Python,
Because that language is beautiful.
'''.format(name)
print(message)
