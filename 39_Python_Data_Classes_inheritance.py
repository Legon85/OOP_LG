from dataclasses import dataclass, field, InitVar
from typing import Any


# в качестве примера наследования классов при использовании декоратора dataclass сформируем класс Goods
# для представления различных товаров и создадим дочерний класс Book
@dataclass
class Goods:
    uid: Any
    price: Any = None
    weight: Any = None


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0


#  как будут у этих классов формироваться инициализаторы? следующим образом:
#  class Goods:
#       def __init__(uid: Any, price: Any = None, weight: Any = None):
#  class Book:
#       def __init__(self, uid: Any, price:float = 0, weight:int | float = 0, title:str = "", author:str = ""):
#  чтоб убедиться в правильности формирования создадим объект без св-тв и с ними и выведем все его св-ва:


b = Book(1)
print(b)  # -> Book(uid=1, price=0, weight=0, title='', author='')
b = Book(1, 1000, 100, "Python OOP", "Mironov A. M.")
print(b)  # -> Book(uid=1, price=1000, weight=100, title='Python OOP', author='Mironov A. M.')


#  теперь усложним задачу и сделаем так, чтоб uid в объектах формировался каждый раз автоматически при
#  создании объекта

#  создадим, во-первых, дополнительный параметр current_uid без аннотации (из-за отсутствия аннотации типов
#  декоратор @dataclass просто не заметит и пропустит параметр current_uid, но в классе он просто будет
#  существовать, что нам и надо)
#  параметр же uid мы аннотируем как целочисленный и исключим из инициализации через field(init=False).
#  В конце объявим метод __post_init__. Он и будет увеличивать current_uid на 1 каждый раз при создании
#  нового объекта и присваивать это значение параметру uid.


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: post_init")  # печатаем только для инициализации сработки метода __post_init__
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0


b = Book(1000, 100, "Python OOP", "Mironov A. M.")  # создаём объект без указания первого параметра uid
print(b)  # -> Book(uid=1, price=1000, weight=100, title='Python OOP', author='Mironov A. M.')


#  Если прописать метод __post_init__ в дочернем же классе в простом виде (будет выводить только строчку
#  "Book: post_init"), то получим ошибку т.к. при создании дочернего класса Book в нём самом уже есть
#  метод __post_init__. __post_init__ ,в свою очередь, вызывается из базового класса только если его не
#  прописано в дочернем. Поэтому __post_init__ из базового класса вызван не будет и uid автоматически не
#  сформируется. Чтоб это исправить надо через super() явно вызвать __post_init__ базового класса Goods:
@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: post_init")  # печатаем только для инициализации сработки метода __post_init__
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0

    def __post_init__(self):
        super().__post_init__()  # явно вызываем post_init из Goods
        print("Goods: post_init")


b = Book(1000, 100, "Python OOP", "Mironov A. M.")
print(b)
# вывод будет следующий:
# Goods: post_init  (вызван post_init для базового класса)
# Goods: post_init  (вызван post_init для дочернего класса, чего и добивались)
# Book(uid=1, price=1000, weight=100, title='Python OOP', author='Mironov A. M.')
