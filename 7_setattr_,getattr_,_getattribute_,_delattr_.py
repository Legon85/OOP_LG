# известно, что для обращения к атрибутам класса MIN_COORD MAX_COORD внутри методов класса нужно использовать
# ссылку на сам класс Point.MIN_COORD / Point.MAX_COORD либо(что правильнее) ссылку на экземпляр self.MIN_COORD
# self.MAX_COORD
class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:  # пример обращения к атрибутам класса внутри метода класса
            self.x = x
            self.y = y

    # НО !!! Когда нам необходимо написать метод изменяющий значения атрибутов класса,то вышеописанный способ со
    # ссылками на экземпляр класса self не подходит по той причине, что в данном случае по сути не будет никакого
    # изменения атрибутов класса, а будет лишь создание локального атрибута экземпляра класса с таким же именем как
    # атрибут класса (MIN_COORD, MAX_COORD) Потому что механизм присваивание значения атрибутам работает таким
    # образом, что сначала ищется атрибут в локальной области и если его там нет, то он просто создаётся)
    def set_bound(self, left):
        self.MIN_COORD = left  # в данном случае не произойдёт изменение атрибута класса MIN_COORD а просто
        # создастся локальный атрибут с именем MIN_COORD


pt1 = Point(1, 2)
pt1.set_bound(-100)
print(pt1.__dict__)  # {'x': 1, 'y': 2, 'MIN_COORD': -100} появилось лок.св-во MIN_COORD = -100
print(
    Point.__dict__)  # {'__module__': '__main__', 'MIN_COORD': 100, 'MAX_COORD': 0, '__init__':  ....}  а значение


# атрибута класса 'MIN_COORD': 100 не изменилось как видим.


# Поэтому если нам необходимо изменить значение атрибутов класса, то нужно пользоваться декоратором @classmethod:
class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:  # пример обращения к атрибутам класса внутри метода класса
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


pt1 = Point(1, 2)
pt1.set_bound(-100)
print(pt1.__dict__)  # {'x': 1, 'y': 2} новых атрибутов не создалось
print(Point.__dict__)  # {'__module__': '__main__', 'MIN_COORD': -100, 'MAX_COORD':  ....} значение атрибута класса


# изменилось 'MIN_COORD': -100


# __setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
# __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно: существует оно или нет).

# В Python когда мы обращаемся к какому-либо атрибуту через экземпляр класса, неявно срабатывает магический
# метод __getattribute__. Чтоб это показать переопределим его и выведем его срабатывание:

class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:  # пример обращения к атрибутам класса внутри метода класса
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        """self - ссылка на экземпляр, item - атрибут, к которому идёт обращение. Метод автоматически вызывается,
        когда идёт считывание атрибута через экземпляр класса """
        print("__getattribute__")  # переопределяем метод для вывода строки с его названием
        return object.__getattribute__(self, item)  # чтобы метод срабатывал его нужно вызвать из базового класса


# теперь каждый раз когда мы будем обращаться к тому или иному атрибуту через экземпляр будет срабатывать
# __getattribute__:
pt1 = Point(1, 2)
pt2 = Point(10, 20)
a = pt1.x  # видим в консоли вывод  __getattribute__ в результате того, что мы обратились к атрибуту x


# экземпляра pt1

# Но где по сути может понадобиться использование такого метода? В качестве примера можно привести следующее:
# Предположим, что мы хотим запретить обращаться напрямую к атрибуту "х" Это можно сделать с использованием метода
# __getattribute__ следующим образом:
class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:  # пример обращения к атрибутам класса внутри метода класса
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":  # если обращаются к атрибуту "х"
            raise ValueError("Доступ запрещён")  # то получаем сообщение о запрете
        else:  # в противном случае если обращаемся к другим атрибута
            return object.__getattribute__(self, item)  # то они будут без проблем возвращаться


pt1 = Point(1, 2)
pt2 = Point(10, 20)
b = pt1.y
print(b)  # 2


# a = pt1.x  # ValueError: Доступ запрещён     РАСКОМЕНТИТЬ ДЛЯ ПРОВЕРКИ


# Следующий метод __setattr__. Неявно вызывается каждый раз когда идёт присвоение какого либо значения атрибуту
# В качестве параметров принимает key - имя атрибута,  value - присваиваемое значение.
# Выведем так же его явно в консоль:

class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:  # пример обращения к атрибутам класса внутри метода класса
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Доступ запрещён")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print("__setattr__")
        object.__setattr__(self, key, value)


pt1 = Point(1, 2)
pt2 = Point(10, 20)


# __setattr__
# __setattr__
# __setattr__
# __setattr__ # получаем 4 раза __setattr__ поскольку было 4 присвоения значений атрибутам
# Point(1, 2)  и  Point(10, 20)

# В качестве примера использования можно по аналогии привести переопределение метода на запрещение присваивания
# определённому атрибуту значения:

class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Доступ запрещён")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)


pt1 = Point(1, 2)
pt2 = Point(10, 20)


# pt1.z = 5  # получаем определённое в методе __setattr__ исключение: AttributeError: недопустимое имя атрибута

# Есть ещё один ньюанс связанный с методом __setattr__: если в его второй части блока if/else прописать не вызов
# из базового класса object а следующее: self.x = value (то есть как бы присвоение определённому атрибуту
# значения value), то сам метод __setattr__ будет вызываться по рекурсии. Поэтому в таком случае надо
# использовать синтаксис "через __dict__": self.__dict__[key] = value
# Поэтому в общем случае просто нужно использовать синтаксис object.__setattr__(self, key, value)
class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Доступ запрещён")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            # object.__setattr__(self, key, value) # в целом лучше пользоваться этим способом
            # self.x = value  # получим: RecursionError: maximum recursion depth exceeded in comparison
            self.__dict__[key] = value  # в данном случае надо делать так


pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.y = 5  # RecursionError: maximum recursion depth exceeded in comparison
print(pt1.y)


# Метод __getattr__ неявно вызывается каждый раз когда идёт обращение к несуществующему атрибуту экземпляра класса.
# Переопределим его для явного срабатывания и вывода информации
class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Доступ запрещён")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print("__getattr__: " + item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.yy)  # получаем: __getattr__: yy и None поскольку обращаемся к несуществующему атрибуту экземпляра pt1


# Пример использования данного метода: Переопределим его так, чтобы, в случае обращения к несуществующему
# атрибуту экземпляра, Python не генерировал исключение, а выводил False
class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Доступ запрещён")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.yy)  # False


# если закомментировать метод __getattr__, то будет выводиться стандартное исключение Python:
# AttributeError: 'Point' object has no attribute 'yy'

# И последний метод __delattr__ неявно вызывается каждый раз когда удаляется атрибут через экземпляр класса
# Переопределим его так, чтобы он выводил информацию о себе и удаляемом атрибуте

class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Доступ запрещён")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__: " + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.x  # получаем вывод переопределённый в методе:   __delattr__: x
print(pt1.__dict__)  # {'y': 2} атрибут "х" между тем удалён
