# добавим ещё одно св-во length в __slots__ класса Point2D:

class Point2D:
    __slots__ = ('x', 'y', 'length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x * x + y * y) ** 0.5


pt = Point2D(1, 2)
print(pt.length) # -> 2.23606797749979 выводим посчитанное св-во length

# теперь обернём св-во length в декоратор property чтоб получать его и изменять

class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

# используя декораторы можно обращаться к приватному св-ву '__length' даже если методы названы
# не такими же именами (а именно: def length)
pt = Point2D(1, 2)
print(pt.length) # -> 2.23606797749979 всё работает


# Теперь рассмотрим как __slots__ ведет себя при наследовании классов:

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Poin3D(Point2D): # создаём класс наследуемый от Point2D
    pass

pt3 = Poin3D(10, 20)
pt3.z = 30
print(pt3.z) # -> 30 мы добавили в объект pt3 свойство z = 30, что в свою очередь означает, что __slots__ не был передан
# в класс Point3D при наследовании
print(pt3.__dict__) # - > {'z': 30}  словарь у этого объекта тоже имеется, соответственно. Но в нём нет приватных свойств
# наследуемых из класса Point2D, хотя вызвать эти св-ва через объект pt3 можно:
print(pt3.x) # -> 10

# для того чтобы объект pt3 тоже мог оперировать только св-вами находящимися в коллекции__slots__
# базового класса Point2D, надо в дочернем классе просто прописать коллекцию __slots__ без каки-либо аргументов
# тогда класс Point3D сам по себе не будет иметь возможности создавать никакие св-ва, но сможет оперировать
# св-вами определёнными в slots базового класса Point2D

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Poin3D(Point2D):
    __slots__ = () # определяем пустой slots в дочернем классе

pt3 = Poin3D(10, 20)
# pt3.z = 30 # для проверки раскомент.
# print(pt3.z) # -> 'Poin3D' object has no attribute 'z' получаем ошибку т.к. теперь доступны только x и y
# print(pt3.__dict__)
# print(pt3.x)
# если же нужна возможность оперировать св-вами из Point3D то можно в slots, находящийся в Point3D,дописывать
# нужные свойства

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Poin3D(Point2D):
    __slots__ = 'z', # прописываем нужное св-во в кортеже slots. И т.к. это кортеж обязательно ставим запятую

pt3 = Poin3D(10, 20)
pt3.z = 30
print(pt3.z) # -> 30 ошибок нет

# чтоб объекты класса Point3D могли полноценно присваивать все три св-ва при создании, остаётся прописать инициализатор
# в классе Point3D:

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Poin3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt3 = Poin3D(10, 20, 30)
print(pt3.z)