player_list = [('mio', 32), ('jelly', 2), ('crryting', 30), ('lucy', 8),
               ('Lily', 9), ('lilei', 6)]

for p in player_list:
    pstr = "球员: %s，号码：%d" % (p[0], p[1])
    print(pstr)

print("--------- f-string -------------")

for p in player_list:
    pstr = f"球员：{p[0].upper()},号码：{p[1]}"
    print(pstr)

a = 2
b = 10
print(f"{a}的{b}次方={a**b}")
print(f"{{{a}}}的{{{b}}}次方={a**b}")

for p in player_list:
    pstr = f"球员：{p[0]:>15s}，号码：{p[1]:02d}"
    print(pstr)


str1 = "Keep calm and do your research!"
loc = str1.find("search")
print(loc)
print(str1[loc:])

str2 = str1.replace('search', 'samling')
print(str1)
print(str2)

strList = str1.split(" ")
print(strList)

str3 = "#".join(strList)
print(str3)

# str.strip() 两边去空格  str.lstrip() 左边去空格   str.rstrip()右边去空格
str1 = "Messi,  10,  striker, Argentina"
strList = str1.split(',')
strList = [s.rstrip() for s in strList]
print('#'.join(strList))

# isdigit()：是否字符串只由数字构成
# isnumeric()：是否全是数字（包括汉字数字）
# isupper()、islower()：是否全大写、全小写
a = '123'
b = '123#'
c = '四十四'
print(a.isdigit(), a.isnumeric())
print(b.isdigit(), b.isnumeric())
print(c.isdigit(), c.isnumeric())

# sort() ：排序 默认从大到小排序
player_list.sort(key=lambda x: x[1], reverse=True)
print(player_list)

