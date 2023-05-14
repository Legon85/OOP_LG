from accessify import private, protected


# public - публичное св-во. К нему можно обращаться напрямую через ссылку на
# экземпляр,
# например,
# а так же изменять его
# напрямую
# _protected - служит для обращения внутри класса и во всех его дочерних классах

# Одно подчеркивание лишь сигнализирует, что св-во является защищённым и переменная на него ссылающаяся является
# внутренней служебной. Но при этом к ней всё так же можно обращаться и изменять её. И служит она лишь для сигнализации
# программисту о том что она не изменяемая

# __privet - служит для обращения внутри класса
# просто так обратиться и изменить __privet уже не получится (получим ошибку).
# Но можно создать внутри класса метод, который будет изменять эти св-ва внутри класса и тогда опять-таки их можно
# изменить. Такие методы называются setter'ами
# Так же можно создать метод внутри класса, который будет обращаться к этим атрибутам внутри класса и выводить их
# значения. Такие методы называются getter'ами
# setter и getter иногда ещё называют интерфейсными методами

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):  # внутренний метод для установки новых значений privet атрибутам (setter)
        self.__x = x
        self.__y = y

    def get_coord(self):  # внутренний метод для вывода privet атрибутов(getter)
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())  # (10, 20)
print(pt.__dict__)  # {'_Point__x': 10, '_Point__y': 20}  св-ва поменялись !!!


# Во всём вышеописанном и есть суть ИНКАПСУЛЯЦИИ. А именно: в ООП есть возможность создавать публичные методы (сеттеры и
# геттеры) для работы с закрытыми методами!!! Что обеспечивает неприкосновенность и безопасность самих внутренних
# атрибутов


# Конечно суть сеттеров и геттеров заключается не только в банальной передаче значений аргументам и обращению к ним.
# Например, перед изменением значений аргументов можно сначала сделать проверку на валидность типа изменяемого значения.
# Сделаем так, чтобы перед изменением значений __x, __y сначала производилась проверка на то, что те значения на которые
# будут ссылаться __x, __y были либо целыми, либо вещественными значениями

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):  # проверка описанная выша
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)


# Можно ещё усовершенствовать класс и добавить туда приватный метод для проверки корректности координат. Для
# универсальности сделаем его методом класса, поскольку он возможно будет обращаться не только к атрибутам объектов
# класс, но и к атрибутам самого класса

class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):  # определяем метод для проверки валидности координат(теперь он универсальный для
        # многих случаев)
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):  # вставляем метод для проверки сюда
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())  # (10, 20)
print(pt.__dict__)

# Рассмотрим ещё один ньюанс! Распечатаем все св-ва экземпляра класса через __dir__
print(dir(pt))  # ['_Point__check_value', '_Point__x', '_Point__y', '__class__', '__delattr__', '__dict__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__'
# , '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_coord', 'set_coord']

# Мы видим что в коллекции есть некие св-ва _Point__x, _Point__y. Это и есть кодовые имена приватных св-тв к которым
# мы не можем обращаться напрямую. И ньюанс в том, что к ним всё равно можно обратится через эти кодовые имена:
print(pt._Point__x, pt._Point__y)  # 10 20


# Но ВНИМАНИЕ!!! ТАК ДЕЛАТЬ СТРОГО НЕ РЕКОМЕНДУЕТСЯ!!!

# Если появилась необходимость полностью ограничить доступ к приватным атрибутам, то можно воспользоваться модулем
# accessify предварительно его установив(pip install accessify) импортировав из него privat and protected

class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private  # определяем декоратор private модуля accessify
    @classmethod
    def check_value(cls, x):  # при этом можно убрать двойное подчёркивание в названии метода(всё равно будет защищён)
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):  # здесь тоже убираем двойное подчёркивание
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
pt.check_value(5)  # accessify.errors.InaccessibleDueToItsProtectionLevelException: Point.check_value() is inaccessible
# due to its protection level(защита с помощью accessify)


