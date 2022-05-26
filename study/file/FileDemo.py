# t：文本文件  b：二进制文件
# r：只读  w：写入，覆盖   a：追加  x：独占写入  +：读写模式

try:
    f = open('something.xxx', 'wb')
except IOError:
    # 错误处理
    print("错误处理")
finally:
    f.close()

# 即使产生异常，也会正确的关闭文件
with open('something.xxx', 'wb') as f:
    # 一些操作
    print('一些操作')

# 指定编码(win系统打开*nix系统的文件)
f = open('something.xxx', encoding='utf8')
# 指定编码(*nix系统打开win系统的文件)
f = open('something.xxx', encoding='gb18030')

# 文本文件操作
# 一次性 写入文件
with open("text.txt", 'wt') as f:
    f.write("a\nb\nc\nd\ne\nf\ng\n")
# 一次性 读取文件
with open("text.txt", 'rt') as f:
    a = f.read();
    print(a)
# 一行一行的读取文件
with open("text.txt", 'rt') as f:
    while True:
        a = f.readline()
        if a == '':
            break
        else:
            print(a)
# 一次读取所有行，返回一个数组，每一个元素代表一行
with open("text.txt", 'rt') as f:
    a = f.readlines()
    # 使用推断语句，将\n去除
    # a = [arr.strip() for arr in a]
    print(a)

# csv文件操作
import csv
# 输出每一行的数据，以","分割
with open('csv/kfc.csv') as f:
    reader = csv.reader(f)
    i = 0
    for r in reader:
        print(r)
        if i >= 5:
            break
        i += 1

# 根据第一行标题，生成每一行的键值对
with open('csv/kfc.csv') as f:
    dic_reader = csv.DictReader(f)
    i = 0
    for r in dic_reader:
        print(r)
        if i >= 5:
            break
        i += 1

