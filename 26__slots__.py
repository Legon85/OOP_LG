import timeit
# предположим есть простой класс
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# создадим экземпляр
pt = Point(1, 2)
# выведем свойства объекта:
print(pt.__dict__) # -> if text[i] == '-' or text[i] == '_'
# изменим одно свойство:
pt.y = 10
# снова выведем:
print(pt.__dict__) # -> {'x': 1, 'y': 10}
# создадим новое лок.св-во:
pt.z = 4
# выведем:
print(pt.__dict__) # -> {'x': 1, 'y': 10, 'z': 4}

# но что если необходимо объявить класс точки на плоскости такой, чтоб у его экземпляров могли быть только свойства
# x и y ,например, и только они и никакие другие!? Для этого и применяется коллекция __slots__


class Point2D:
    __slots__ = ('x', 'y') # здесь мы записываем, в виде строк, какие локальные свойства будут разрешены экземплярам
    # этого класса. Именно локальные, а не атрибуты самого класса Point2D
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt2 = Point2D(10, 20)
print(pt2.x) # -> 10
print(pt2.y) # -> 20
# pt2.z = 30 # -> AttributeError: 'Point2D' object has no attribute 'z' ошибка т.к. экземпляры этого класса
# могут использовать только лок. св-ва x и y которые записаны в __slots__

# еще один момент связанный со __slots__ :  при использовании __slots__ не формируется словарь со свойствами
# pt2.__dict__

# print(pt2.__dict__) # ->AttributeError: 'Point2D' object has no attribute '__dict__'  ошибка!!!

# все остальные привычные действия именно с лок. св-вами x и y можно делать (изменять, удалять, обратно создавать)\

# при чём всё это касается исключительно лок. св-тв экземпляров. А с атрибутами класса можно продолжать работать в
# в том же режиме например:
class Point2D:
    __slots__ = ('x', 'y')
    MAX_COORD = 100 # без проблем создаём ещё один атрибут класса


    def __init__(self, x, y):
        self.x = x
        self.y = y


pt2 = Point2D(10, 20)
print(pt2.MAX_COORD)  # атрибут без проблем выводится через экземпляр

# так же при использовании __slots__ занимется меньше памяти. это можно проверить так
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point2D:
    __slots__ = ('x', 'y')


    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(10, 20)
pt2 = Point2D(10, 20)

print(pt.__sizeof__() + pt.__dict__.__sizeof__()) # -> 120  вывели количество занимемой памяти(без slots)
print(pt2.__sizeof__()) # -> получаем 32 т.к. коллекцию __dict__ данный вариант не содержит в отличии верхнего


# ещё при использовании slots ускоряется работа с переменными x и y. Например:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self): # учебный прмер в котором производится некая работа с лок. св-вами для замера времени
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self): # учебный прмер в котором производится некая работа с лок. св-вами для замера времени
        self.x += 1
        del self.y
        self.y = 0


p = Point(1, 2)
p2 = Point2D(10, 20)

t1 = timeit.timeit(p.calc) # модуль timeit импортирован вначале файла!
t2 = timeit.timeit(p2.calc)
print(t1) # -> 0.4291901999968104
print(t2) # -> 0.3654570000071544  метод со slots отрабатывает быстрее!!!