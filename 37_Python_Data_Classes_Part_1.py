# Довольно часто на практике приходится для создания объектов класса определять однотипные инициализаторы,например:

from dataclasses import dataclass,field
from pprint import  pprint


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

# кроме этого,чтоб при вызове print(t) (ссылки на объект этого класса) не выводилась не вполне информативная
# информация вида: <__main__.Thing object at 0x00000259CE3C5AB0> нужно прописывать метод __repr__:

    def __repr__(self):
        return f"Thin: {self.__dict__}" #->Thin: {'name': 'Учебник по Python', 'weight': 100, 'price': 1024}


t = Thing("Учебник по Python", 100, 1024)
print(t)



# для автоматизации этих процессов с версии Pthon 3.7 можно использовать инструмент - DataClasses
# с использованием декоратора dataclass посредством импорта из модуля dataclasses,внутри которого уже
# прописаны методы init, repr а так же eq для автоматизации процесса создания объектов
# Для правильной работы такого способа атрибуты в этом классе обязательно должны быть аннотированы!!

@dataclass
class ThingData:
    name: str
    weight: int
    price: float


td = ThingData("Учебник по Python", 100, 1024)
print(td) #-> ThingData(name='Учебник по Python', weight=100, price=1024)

# с помощью ф-ции pprint из модуля pprint можно посмотреть на структуру класса ThingData
pprint(ThingData.__dict__)

# теперь создадим 2ой оъект ThingData c другими параметрами и сравним с первым:
td_2 = ThingData("Python OOP", 80, 512)
print(td == td_2)#-> получаем ожидаемое False
#но если создать ещё один объект с точно такими же параметрами и сравинить их:
td_3 = ThingData("Python OOP", 80, 512)
print(td_2 == td_3) #-> получаем True
# Во втором случае получили True потому,что при создании объектов через dataclass, их сравнение происходит
# по принципу сравнения на идентичность их локальных св-тв, а не id-шников, как это присходит при обычном
# создании объектов. dataclass переопределяет метод __eq__ отвечающий за сравнение объектов так, чтоб он
# сравнивал не id объектов,а их локальные св-ва полученные при иницализации

# если,например, нам не нравится, что сравнение происоходит по всем трём св-вам объекта, а нам надо чтоб
# происходило только по атрибуту weight, то это можно самостоятельно переопределить в методе __eq__:

@dataclass
class ThingData:
    name: str
    weight: int
    price: float

    def __eq__(self, other): # переопределяем метод согласно вышеописанному требованию
        return self.weight == other.weight


td = ThingData("Учебник по Python", 100, 1024)
td_2 = ThingData("Python OOP 2 ", 80, 1000)
td_3 = ThingData("Python OOP", 80, 512)
# теперь не все наши параметры при создании объекта равны(только weight), но сравнение всё равно вернёт True
# т.к. метод переопределён под параметр weight
print(td_2 == td_3) # -> True
# то есть если метод __eq__ переопределён,то интерпретатор будет отрабатывать по нему, а если нет, то будет
# работать по умолчанию сравнивая все заданные параметры
# то же самое работает и с методами __init__ и __repr__ встроенными в dataclass. Но с другими встроенными не всегда так.

# так же можно указывать парамтры со значениями по-умолчанию:

@dataclass
class ThingData:
    name: str
    weight: int
    price: float=0 # по-умолчанию

    def __eq__(self, other): # переопределяем метод согласно вышеописанному требованию
        return self.weight == other.weight


td = ThingData("Учебник по Python", 100)
print(td) # ThingData(name='Учебник по Python', weight=100, price=0)
# но те параметры, что мы уазваем по-умолчанию должны записываться в конце(после обычных позиционных параметров)

# существует еще один тонкий момент связанный с присваиванием параметрам значений представляющих из себя
# изменяемые объекты. Например:
class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

t = Thing("Учебник по Python", 100, 1024)
# если мы далее добавим в dims значение:
t.dims.append(10)
print(t.dims) # -> 10
# а потом создадим объект t2
t2 = Thing("Учебник по Python", 100, 1024)
# и выведем у него значение dims,то получим уже существующее значение dims = 10
print(t2.dims)# -> 10
# Но! такое поведение является неблагоприятным и ошибочным! Такое происходит потому,что инициализатор
# срабатывает для всех создающихся объектов и список в параметре dims=[] будет един по ссылке к нему
# для всех объектов, что означает что с каждым новым объектом этот список будет лишь пополняться а не
# обнуляться. А мы бы естесственно хотели,чтоб он был для каждого нового объекта вновь путсым

# поэтому в dataclasses нельзя напряму по-умолчанию присваивать какие-либо изменяемые объекты
# например елси прописать изменяемый объект, то получим ошибку
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: float=0
#     dims: list = [] #-> ValueError: mutable default <class 'list'> for field dims is not allowed: use default_factory

# для того чтоб реализовать возможность добавления изменяемых объектов используется ф-ция field() и
# портируемый из того же модуля что и dataclasses c параметром defaukt_factory. Тогда все будет работать
@dataclass
class ThingData:
    name: str
    weight: int
    price: float=0
    dims: list = field(default_factory=list)

td = ThingData("Учебник по Python", 100, 1024)
print(td)# ThingData(name='Учебник по Python', weight=100, price=1024, dims=[])
td.dims.append(10) # добавляем 10 в dims
print(td) # ThingData(name='Учебник по Python', weight=100, price=1024, dims=[10])
td2 = ThingData("Учебник по Python", 100, 1024)# создаём td2
print(td2)# но теперь dims в td2 пуст. Что нам и нуждно!