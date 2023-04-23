# если создать неки класс Geom и после его создания, прописав его ниже, поставить точку,
# то автоматически подсветятся целый ряд методов,которые мы можем использовать с этим классом
# но откуда они беруться елси они не определены в нашем классе - из базового класса object
class Geom:
    pass

print(Geom.__name__)

# по сути происходит следующее:
# запись "class Geom:" эквивалентна записи "class Geom(object)":, где явно видно наследование класса
#  Geom от класса object. Просто с определённой версии Python
#  запись базового класса object (в скобках) можно опускать
# но если создать класс Line наследуемы от Geom:
class Geom: # -->  class Geom(object):
    pass

class Line(Geom):
    pass

g = Geom()

# то непосредственного наследования класса Line от класса
# object уже не будет. Будет сначала Line наследоваться от Geom, а Geom уже от object
# но все атрибуты класса object будут доступны экземплярам класса Line т.к. вызов их будет
# осуществляться по цепочке: class Geom --> class object-->атрибуты класса object
l = Line()
print(l.__class__)

#чтоб определять является какой-то класс подклассом другого класса изпользуется ф-ция issubclass()
# передавать ей в качестве аргументов можно только классы (не аргументы - будет ошибка)
print(issubclass(Line, Geom)) # --> True
print(issubclass(Geom, Line)) # --> False
# чтоб проверить принадлежность объекта классу используется isinstance()
print(isinstance(l, Geom)) # --> True
print(isinstance(l, object)) # --> True

# все стандартные типы данных python ( int, float, list, tuple, set...) так же являются классами
print(isinstance(int, object)) # --> True
print(isinstance(list, object)) # --> True

# поэтому любой встроенный класс python можно как-либо расширить. наприер:

class Vector(list):
    def __str__(self):
        """ переопределение метода str для класса list чтоб вывод значений через был через пробел, а не
        через запятую"""
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v) # --> 1 2 3
# и,кстати после этот если прописать "type(v)" то получим уже не list а <class '__main__.Vector'>
print(type(v))