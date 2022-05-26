import pickle


class Cat:
    def __init__(self, name, weight=None, age=None):
        self.name = name
        self.__weight = weight
        self.__age = age
        print("cat ", self.name, " is created.")

    def get_weigth(self):
        return self.__weight

    def get_age(self):
        return self.__age

    def set_weight(self, weight):
        self.__weight = weight

    def set_age(self, age):
        self.__age = age

    def shout(self):
        print("喵~")

    def catch(self):
        print("\N{rat}")


lucas = Cat("Lucas", weight=10, age=1)
# 写文件 将python类数据写入文件
with open('Lucas.py', 'wb') as f:
    pickle.dump(lucas, f)

# 读文件 将存储的python类数据读取出来
with open('Lucas.py', 'rb') as f:
    lucas2 = pickle.load(f)

lucas2.shout()
print(lucas2.get_age())
