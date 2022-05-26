print("Hello World")


class Demo:
    _weight = 8.5

    def get_weight(self):
        return self._weight


lucas = Demo()

try:
    print("weight of lucas",lucas._weight)
except Exception as e:
    print(e)
lucas._weight = 9
print("weight of lucas", lucas._weight)
print("weight of lucas", lucas.get_weight())


class Felidae:
    def __init__(self, name, weight=None, age=None):
        self.name = name
        self.__weight = weight
        self.__age = age
        print("cat", self.name, "is createed")

    def get_weight(self):
        return self.__weight

    def get_age(self):
        return self.__age

    def set_weight(self, weight):
        self.__weight = weight

    def set_age(self, age):
        self.__age = age

    def catch(self):
        pass


lucas_felidae = Felidae("little_cat", weight=8.5, age=1.2)
print(lucas_felidae.get_age(), lucas_felidae.get_weight())
lucas_felidae.set_age(2.5)
print(lucas_felidae.get_age(), lucas_felidae.get_weight())


class Cat(Felidae):
    def __init__(self, name, weight=None, age=None, color=None):
        super().__init__(name=name, weight=weight, age=age)
        self.color = color

    def shout(self):
        print("喵~")

    def catch(self):
        print("\N{rat}")


class Lion(Felidae):
    def __init__(self, name, weight=None, age=None, sex=None):
        super().__init__(name=name, weight=weight, age=age)
        self.sex = sex

    def catch(self):
        print("\N{rabbit}")


print("-----------Lucas------------------")
lucas = Cat("Lucas", color="三花", age=2)
lucas.catch()
lucas.shout()
print(lucas.get_age())
print("-----------Simba------------------")
simba = Lion("Simba", weight="200", age=4, sex="male")
simba.catch()
print(simba.get_weight())

