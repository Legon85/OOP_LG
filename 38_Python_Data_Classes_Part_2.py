from dataclasses import dataclass, field,InitVar

# предположим что нам в классе Vector3D нужно определить некоторое вычисляемое св-во length = (x * x + y * y + z * z) ** 0.5:
# class Vector3D:
#     def __init__(self, x: int, y: int, z: int):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.length = (x * x + y * y + z * z) ** 0.5

# как это можно сделать при объявлении класса через dataclass? -
# иницилизаторы которые срабатывают в декораторе detaclass имеют специальный метод __post_init__ и как  раз
# в этот метод (в нём уже имеются все атрибуты прописанные в __init__) и прописывается вычисляемый атрибут

@dataclass
class V3D:
    x: int
    y: int
    z: int

    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v) #-> V3D(x=1, y=2, z=3)
# но при этом мы не видим сформированного св-ва length потому, что когда декоратор dataclass формирует
# магический метод repr то он заносит в него только те св-ва которые прописаны явно,а не те,что мы
# прописываем налету внутри инициализатора __post_init__
# как выйти из этой ситуации? - прописать его в общем списке параметров но при этом сделать так,чтоб он
# не прописывался в инициализаторе с помощью синтаксиса fieald(init=False)

@dataclass
class V3D:
    x: int
    y: int
    z: int
    length: float = field(init=False)

    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v) #-> V3D(x=1, y=2, z=3, length=3.7416573867739413) теперь length=3.7416573867739413 присутствует

# ф-ция field() так же может принимать и ещё ряд полезных параметров:
# repr - булевое значение True/False указывает использовать ли атрибут в магическом методе __repr__()(по умаолчанию True)
# compare - булевое значение rue/False указывает использовать ли атрибут при сравнении объектов(по умолчантю True)
# defaukt - значение по умолчанию (начальное значение)

# пробуем использовать эти параметры field():

@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    length: float = field(init=False, compare=False)

    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v) #-> V3D(y=2, z=3, length=3.7416573867739413)
# в данном случае мы во-первых не видим в выводе информации,определённой методом __repr__, свойства x,
# потому,что определили ему field(repr=False)
# во-вторых если создать объект v2 с отличным от v1 параметром z: то мы получим True потому,что мы исключили
# z и length из сравнения посредством синтаксиса z: int = field(compare=False)
v2 = V3D(1, 2, 5)
print(v)
print(v2)
print(v == v2) #-> False

# Предположим мы бы хотели вычислять длину вектора length в зависимости от некоторого параметра calc_len.
# Делается это следующим образом: Этот параметр (calc_len) указывается в классе в качестве параметра. И он
# аннотируется специальным классом InintVar из того же модуля dataclasses. Любой параметр аннотированый через
# InitVar автоматически передаётся в метод __post_init__, где и находится вычисление длины length. И, в
# зависимости от того что принимает calc_len (True/False) будет срабатывать или нет вычисление длины

@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len:bool):
        if calc_len: # теперь если calc_len = True,то будет работать self.len а если False, то будет ставиться
            # значение по умолчанию(в нашем случае default=0)
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5



v = V3D(1, 2, 3, True) # теперрь length вычисляется только если calc_len=True
print(v)

# До сих пор декоратор dataclass использовался без параметро. На самом деле он может принимать целый ряд
# параметров. Наиболее часто используемые из них:

# Параметр init принимает по умолчанию True. Если False, то в классе не объявляется инициализатор!Полезен но
# когда нужно создать какой-либо класс в качестве базового,который не подразумевает инициализации никаких
# параметров:
@dataclass(init=False)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len:bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5



# v = V3D(1, 2, 3, True)
# print(v) # т.к. в @dataclass параметр init=False получаем ошибку - TypeError: V3D() takes no arguments

# Параметр repr принимает по умолчанию True. Если False, то в классе не объявляется __repr__!
@dataclass(repr=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len:bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5



v = V3D(1, 2, 3, True)
print(v) # поскольку параметр repr=False,то при выводе обекта получаем <__main__.V3D object at 0x00000231D7453AC0>
# а не V3D(y=2, z=3, length=3.7416573867739413) как по умолчанию задумано

# Параметр eq принимает по умолчанию True. Если False, то в классе не объявляется __eq__!


@dataclass(eq=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len:bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5



v = V3D(1, 2, 3, True)
v2 = V3D(1, 2, 3, True)
print(v == v2) # получаем False т.к. eq=False и объекты сравниваются по idшникам а не по св-вам

# Параметр order принимает по умолчанию False. Если True, то в классе объявляется магические методы для
# оперций сравнения <, <=, >, >=
@dataclass(eq=True, order=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len:bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3, True)
v2 = V3D(1, 2, 3, True)
print(v < v2) # получаем False,что верно. А значит у нас работает метод order=True. Но этот параметр
# работает только если метод eq тоже находится в True т.к. он от него зависит. А так же при включенном
# методе order нельзя прописывать сви собственные методы сравнения для операций <, <=, >, >=

# Параметр frozen принимает по умолчанию False. Если True, то атрибуты объектов класса становятся неизменными
# (можно только проинициализировать один раз в инициализаторе)
@dataclass(frozen=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len:bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3, True) # Получаем ошибку dataclasses.FrozenInstanceError: cannot assign to field 'length'
# поскольку Frozenset запретил нам изменять св-ва объекта, но мы пытаеся это сделать в методе __post_init__

# Параметр slots принимает по умолчанию False. Если True, то атрибуты объявляются в коллекции __slots__

# Параметр unsafe_hash влияет на формирование магического метода __hash__