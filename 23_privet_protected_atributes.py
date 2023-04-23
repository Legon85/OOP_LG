#  сделаем все локал.свойства для образующихся объектов из из базового класса приватными
class Geom:
    name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.__x1 = x1  # --> приватное
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2) # "делегирование"
        self.__fill = fill

# получим не просто словарь со свойствами объекта r, а следующего вида словарь( с добавлением префикса _Geom),
# не смотря на то, что self является ссылкой на объект класса rect, и лишь свойство fill, прописанное непосредственно
# в классе Rect будет иметь префикс _Rect)
r = Rect(0, 0, 10, 20)
print(r.__dict__) # --> {'_Geom__x1': 0, '_Geom__y1': 0, '_Geom__x2': 10, '_Geom__y2': 20, '_Rect__fill': 'red'}

# из этого следует, что мы не можем обращатся к свойствам __x1, __y2 и т.д. из дочернего класса Rect
# пример:
class Geom:
    name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.__x1 = x1  # --> приватное
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2) # "делегирование"
        self.__fill = fill

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self.__x1, self.__y1)


r = Rect(0, 0, 10, 20)
# r.get_coords() # получаем ошибку: (для проверки раскоментировать)
# -->  'Rect' object has no attribute '_Rect__x1'. Did you mean: '_Geom__x1'?

# но если перенести метод get_coords в базовый класс,то всё будет работать:
class Geom:
    name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.__x1 = x1  # --> приватное
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self.__x1, self.__y1)



class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill


r = Rect(0, 0, 10, 20)
print(r.get_coords()) # --> (0, 0) ошибок нет

# вся суть тут заключается в том что приватные атрибуты жёстко привязываются к текущему классу
# и из дочернего например из вызвать уже не получится и наоборот


# чтобы была возможность использовать закрытые атрибуты в текущем классе,
# то надо использовать не privet а protected атрибуты с одним подчёркиванием
# пример:
class Geom:
    name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1  # --> приватное
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self.__x1, self.__y1)



class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self._x1, self._y1)



r = Rect(0, 0, 10, 20)
print(r.get_coords()) # --> (0, 0) ошибок нет
print(r._x1)  # --> 0    ошибок нет

# тоже самое касается например свойства базового класса name если его сделать privet
# например сейчас можно вывести это свойство через объект класса r.name:
class Geom:
    name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1  # --> приватное
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self.__x1, self.__y1)



class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self._x1, self._y1)



r = Rect(0, 0, 10, 20)
print(r.name) # -> Geom

# но если name  сделать privet  то вызвать его уже не получится
# пример:
class Geom:
    __name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1  # --> приватное
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self.__x1, self.__y1)



class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill
        self.__name = Geom.__name # попытка использовать privet атрибут в дочерем классе(ошибка!)

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self._x1, self._y1)



# r = Rect(0, 0, 10, 20)
# print(r.name) # -> 'Rect' object has no attribute 'name' получаем ошибку( раскоментить для проверки)


# поэтому privet атрибут __name можно использовать только внутри базового класса
# пример:
class Geom:
    __name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1  # --> приватное
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name # переопределение прав доступа из privet в protected


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self._x1, self._y1, self._name)



r = Rect(0, 0, 10, 20)
print(r.get_coords()) # --> (0, 0, 'Geom') получили свойство _name

# тоже самое отностися и privet методам и они могут вызываться только в том классе в котором он определён
# пример:

class Geom:
    __name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.__verify_coord(x1)
        self._x1 = x1  # --> приватное
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name # переопределение прав доступа из privet в protected

    def __verify_coord(self, coord):
        return 0 <= coord < 100


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self._x1, self._y1, self._name)



r = Rect(0, 0, 10, 20)
print(r.get_coords())
print(r.__dict__)


# если __verify_coord прописать Rect то будет ошибка:
class Geom:
    __name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1  # --> приватное
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name # переопределение прав доступа из privet в protected

    def __verify_coord(self, coord):
        return 0 <= coord < 100


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__verify_coord(x1) # попытка прописать приватный метод из базового класс(даст ошибку)
        self._fill = fill

    def get_coords(self): # пример фукции пытающейся использовать свойтсва __x1, __y1 и т.д.
        return (self._x1, self._y1, self._name)



r = Rect(0, 0, 10, 20)
print(r.get_coords())
print(r.__dict__)
# видим ошибку  'Rect' object has no attribute '_Rect__verify_coord'. Did you mean: '_Geom__verify_coord'?