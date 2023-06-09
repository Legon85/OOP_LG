# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0

# используем функцию для создания своего собственного метакласса
def creat_class_point(name, base, attrs):
    """простейшив вид функции реализующей метакласс"""
    return type(name, base, attrs) # соответственно тут она возвращает уже известный класс на основе метакласса

# но в ней должны автоматически добавляться атрибуты MAX_COORD = 100  MIN_COORD = 0

def creat_class_point(name, base, attrs):
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0}) # добавляем в словарь attrs атрибуты MAX_COORD = 100  MIN_COORD = 0
    return type(name, base, attrs)


class Point(metaclass=creat_class_point):# вставляем нашу ф-цию с использованием специального параметра metaclass
    # и передавая ему ссылку на наш метакласс создаваемы этой функцией
    def get_coords(self): # так же указываем в классе метод для примера get_coords
        return (0, 0)

# когда отарбатывает ф-ция creat_class_point ей передаётся в качестве аргументов имя создаваемого класса-Point,
# base у нас остаётся пустой и в attrs попадают все определённые в классах методы: get_coords, а так же посредством
# обновления словаря в этой ф-ции задаются атрибуты MAX_COORD MIN_COORD и затем в return type(name, base, attrs)
# формируется наш новый класс Point c заданными атрибутами и методами


pt = Point() # создаём объект нашего класса и обращаемся к атрибутам ниже
print(pt.MAX_COORD) # -> 100
print(pt.get_coords()) # -> 0
print()



# Но на практике чаще используют отдельные классы, которые игарют роль метакалссов, вместо использования ф-ций:

class Meta(type): # создаём класс наследуемый от метакласса type
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs) # тут вызываем инициализатор базового класса
        cls.MAX_COORD = 100 # динамически добавляем нужные атрибуты
        cls.MIN_COORD = 0

class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


# В данном случае(при создании класса Point) происходит следующее: сам класс Point тут, при своём создании,
# срабатывает подобно создаваемому объекту!!! Для него,как при создании объекта,срабатывает инициализатор
# __init__ в родительском классе Meta,который в качестве аргументов (как при создании объекта) принимает
# ссылку на созданый объект.A в нашем случае это класс Point поэтому ссылка будет иметь вид не self,а cls
# (т.к. является ссылкаой на класс) и далее, по подобию срабатывания метода __init__ для объектов,
# прописываются остальные атрибуты, которые присваиваются объекту(в нашем случае класс Point), а именно :
# (cls, name, base, attrs):
# name(имя создаваемого класса - Point), base(кортеж из базовых классов, attrs(добавляемые атрибуты).
# В добавляемые атрибуты будут автоматически заноситься get_coords,
# MAX_COORD, MIN_COORD будут создаваться динамически т.к. ,поскольку мы используем метод __init__,
# на момент их создания класс Point уже существует(т.к. __init__ срабатывает сразу ПОСЛЕ! создания
# объекта/класса


pt = Point()
# print(Point.__dict__)
print(pt.MAX_COORD) # -> 100
print(pt.get_coords()) # -> 0
print()


# сделаем то же с помощью переопределения магич. метода new :
class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)

class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)



# В данном случае класс Point (как объект) создаётся посредством явного определения метода __new__
# (который,как известно,срабатывает ещё перед созданием объекта). При этом в качестве параметров
# в методе __new__   cls уже будет ссылкой на класс Meta, ну а остальные: name, base, attrs будут
# выполнять туже роль. Только в данном случае атрибуты MAX_COORD, MIN_COORD будут добавляться через
# словарь attrs методом update. Ну и,как полагается в методе __new__, он будет возвращать нам адрес
# на созданный объект через вызов метода __new__ из базового класса type, которы внутри класса type
# запустит создание объекта (в нашем случае Point, потому что у нас Point играет роль объекта
# создаваемого от класса Meta)


pt = Point()
print(pt.MAX_COORD) # -> 100
print(pt.get_coords()) # -> 0
