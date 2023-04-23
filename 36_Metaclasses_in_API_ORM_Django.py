# приведём пример использования пользовательского метакласса  в API ORM Django
# допустим у нас есть некий класс который в качестве атрибутов имеет несколько строк:

# class Women():
#     title = 'заголовок'
#     content = 'контент'
#     photo = 'путь к фото'

# Теперь нам нужно создать класс собственный метакласс, который позволял бы в объектах класса Women сразу
# формировать локоальные св-ва с именами соответствующими св-вам в классе Women и с тем же содержимым:

class Meta(type):
    def creat_local_attrs(self, *args, **kwargs): # 4 ф-ция выполняющая роль инициализатора класса Women
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value # идёт формирование св-тв a b c (см.класс Women) из класса Women
            # для объектов каласса Women

    def __init__(cls, name, bases, attrs):  # 1 инициализатор для создания свойств класса Women
        cls.class_attrs = attrs # 2 определение св-ва class_attrs классу Women
        cls.__init__ = Meta.creat_local_attrs # 3 инициализатор для создания св-тв объектов класса Women!


class Women(metaclass=Meta):
    title = 'заголовок' # a эти св-ва передаются в словарь attrs в инициализаторе класса Meta
    content = 'контент' # b
    photo = 'путь к фото' # c

w = Women()
print(w.__dict__) #->{'__module__': '__main__', '__qualname__': 'Women', 'title': 'заголовок', 'content': 'контент', 'photo': 'путь к фото'}


# то есть по сути класс Meta превращает наш класс Women из такого вида:

# class Women():
#     title = 'заголовок'
#     content = 'контент'
#     photo = 'путь к фото'

# в такой вид:

# class Women(metaclass=Meta):
#     title = 'заголовок'
#     content = 'контент'
#     photo = 'путь к фото'
#
#     def __init__(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value