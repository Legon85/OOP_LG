import math
# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):  #
#         print('__call__')
#         self.__counter += 1
#         return self.__counter


# c = Counter()
# c2 = Counter()
# c()
# c()
# res = c()
# res2 = c2()
# print(res, res2)


# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, step=1, *args, **kwargs):  # добавление аргументов в __call__
#         print('__call__')
#         self.__counter += step
#         return self.__counter


# c = Counter()

# c2 = Counter()
# c()
# c(2)
# res = c(10)
# res2 = c2(-5)
# print(res, res2)

# пример использования метода __call__ в классе вместо замыкания в фукциях:
# -----------------------------------------------------------------------
class StringChars:
    def __init__(self, chars):
        self.__chars = chars # устанавливаем символы для удаления в качестве свойства экземляра

    def __call__(self, *args, **kwargs): # описание метода реализующего вызов экземляров!!!
        if not isinstance(args[0], str): # проверка чтобы входная информация была строчного типа
            raise TypeError('аргумент должен быть строкой')


        return args[0].strip(self.__chars) # отбрасывание всех ненужных символов


s1 = StringChars("?:!.; ")
s2 = StringChars(" ")
print(s1(" Hello world !!!")) # вызов экземпляра посредством метода __call__
print(s2(" Hello world !!!")) # пример создания нескольких разных экземпляров


# эквивалентная ф-ция с замыканием:
#  ----------------------------------------------------

# def strip_string(strip_chars=' '):
#     def do_strip(string):
#         return string.strip(strip_chars)
#
#     return do_strip
#
#
# strip1 = strip_string()
# strip2 = strip_string('?:!.; ')
#
# print(strip1(" Hello world!"))
# print(strip2(" Hello world!"))

# реализация декоратора с помощью __call__
# ________________________________________________________________
class Derivate:
    def __init__(self, func): # func - функция, функционал которой будем расширять декоратором
        self.__fn = func

    def __call__(self,  x, dx=0.0001, *args, **kwargs):  # здесь метод __call__ расширяет функционал df_sin
        return (self.__fn(x+dx) - self.__fn(x)) / dx

# @Derivate
def df_sin(x): # функция для которой был сделан декоратор выше
    return math.sin(x)


print(df_sin(math.pi/3))

df_sin = Derivate(df_sin) # 1ый способ - обернули ф-цию df_sin в класс-декоратор Derivate
# в данно случае df_sin является экземпляром класса Derivate и после её вызова df_sin()
# запустится(сработает) метод __call__
# print(df_sin.__dict__)
print(df_sin(math.pi/3))
# второй способ - поставить @Derivate над исходной функцией и закоментить вышеуказанную строчку


