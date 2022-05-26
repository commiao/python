import re

pattern = r"(\w+\.)*\w+@(\w+\.)+[A-Za-z]+"
# message = "邮箱地址： si.jichun@outlook.com"
# message = "si.jichun@outlook.com"
message = "si.jichun@outlook.com我的邮箱地址"


# match是从第一个字符开始匹配
res = re.match(pattern, message)
print("match结果：", res)
if res is not None:
    print("位置：", res.span())
    print("开始位置：", res.start())
    print("结束位置：", res.end())
    print("匹配的字符串：", res.group())
    print("匹配的字符串：", message[res.start():res.end()])

# search是找到第一个匹配
res = re.search(pattern, message)
print("search结果", res)
if res is not None:
    print("位置：", res.span())
    print("匹配的字符串：", res.group())


# finditer是找到所有的匹配
message = """
我的邮箱地址：si.jichun@outlook.com。
或者，你可以使用：zhiyuezen@126.com。
"""
res = re.finditer(pattern, message)
print("finditer结果", res)
for r in res:
    print(r.group(), ";start:", r.start(), "end:", r.end())


# sub用于替换字符串
res = re.sub(pattern, "就不告诉你", message)
print(res)


# subn用于替换字符串，并返回替换的次数
res = re.subn(pattern, "就不告诉你", message)
print(res[0])
print("替换了：", res[1], "次。")

# 正则表达式提前编译
pattern = re.compile("(\\w+\\.)*\\w+@(\\w+\\.)+[A-Za-z]+")
res = pattern.match(message)
print("匹配的字符串：", message[res.start():res.end()])

res = pattern.search(message)
print("匹配的字符串：", message[res.start():res.end()])

res = pattern.finditer(message)
for r in res:
    print(r.group(), ";start:", r.start(), "end:", r.end())

res = pattern.sub(message)
print(res)

res = pattern.subn(message)
print(res[0])
print("替换了：", res[1], "次。")



