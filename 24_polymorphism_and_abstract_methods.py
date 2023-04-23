# создадим классы фигур и методы вывода их периметров
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_pr(self):
        return 2 * (self.w+self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4 + self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
print(r1.get_rect_pr(), r2.get_rect_pr()) # -> вывод периметров прямоугольников
print(s1.get_sq_pr(), s2.get_sq_pr())

# создадим список из вышесозданных объектов:
geom = [r1, r2, s1, s2]
# теоритически методом перебора списка можно попробовать вызвать методы этих объектов:
# for g in geom:
#     print(g.get_rect_pr())
# но поскольку у объектов разные методы
# то выведутся только результаты 6 и 14 и получим ошибку ->'Square' object has no attribute 'get_rect_pr'
# Как можно правильно поправить эту ситуацию? :
# добавим ещё одну фигуру - треугольник
# !!! и методы возвращающие периметры фигур во всех классах назовём одинаковым именем get_pr
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w+self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 + self.a

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self): # метод называется одинаково
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom = [r1, r2, s1, s2, t1, t2]

# тогда все методы отарботают в цикле как надо:
for g in geom:
    print(g.get_pr())

# !!! это и есть ПОЛИМОРФИЗМ -
# возможность работы с совершенно разными объектами языка Python единым образом
# но если ,например, в одном из классов забыть прописать метод ger_pr(),
# то при обходе цикла мы опять получим ошибку(для проверки закоментировать метод get_pr(),
# например, в классе Triangle
# чтобы решить этот вопрос надо создать отдельный (базовый) класс, в котором будет метод
# get_pr() возвращать некое значение по-умолчанию, напр. -1.
# и тогда, если метод не будет найден в каком-либо из дочерних классов, то сработает метод
# из базового класса и вернёт то значение по-умолчанию
class Geom:
    def get_pr(self):
        return -1


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w+self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 + self.a

class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_pr(self):
    #     return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom = [r1, r2, s1, s2, t1, t2]

# тогда все методы кроме класса Triangle отработают в штатном режмие, а т.к.в Triangle закоментирован метод,
# то сработает метод из базового класса и вернёт -1:
for g in geom:
    print(g.get_pr())


# либо же,что ещё лучше, воспользоваться исключением вместо возвращения значения по-умолчанию.
# тогда программисту будет легче понять что в каком-либо классе отсутствует метод запрашиваемый
# в цикле. Пример:

class Geom:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть переопределён метод get_pr()')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w+self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 + self.a

class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_pr(self):
    #     return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom = [r1, r2, s1, s2, t1, t2]

# тогда все методы кроме класса Triangle отработают в штатном режмие, а т.к.в Triangle закоментирован метод,
# то сработает метод из базового класса и вернёт нам в этот раз исключение:
for g in geom:
    print(g.get_pr())

# в Python методы,которые нужно обязательного переопределять в дочерних классах и которые не имеют собственной реализации
# называются АБСТРАКТНЫМИ!!!