class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


v = Vector(1, 2)
# из выше рассмотренных занятий известно, что например для того чтоб нам вывести значения локальные
# св-тв x и y есть два способа:
# через экземпляр:
print(v.get_coords())  # (1, 2)
# А так же через класc. Только в данном случае надо явно передать ссылку на экземпляр v:
print(Vector.get_coords(v))  # (1, 2)


# Но можно создать св-ва самого класса и обращаться к ним напрямую посредством декоратора @classmethod.
# В данном случае в качестве первого обязательно аргумента методов указывается ссылка на сам класс - cls
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """возвращает TRUE если значение аргумента args укладывается в диапазон от MIN_COORD до
        MAX_COORD """
        return cls.MIN_COORD <= arg <= cls.MAX_COORD  # прямое обращение к св-вам класса

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def validate_1(self, min_coord, max_coord):  # обычный метод объекта
        """возвращает TRUE если значение аргумента x укладывается в диапазон от min_coord до
        max_coord """
        return min_coord <= self.x <= max_coord

    def get_coords(self):
        return self.x, self.y


v = Vector(1, 2)

# в случае с вызовом обычного метода validate_1 через класс Vector нужно использовать в качестве
# первого аргумента ссылку на объект:
print(Vector.validate_1(v, 0, 10))  # True

# В случае же с вызовом метода в декораторе @classmethod можно вызывать напрямую от имени класса без
# ссылок на instance(объект)
print(Vector.validate(5))  # True

# так же класс-метод validate можно вызывать от имени объекта v:
print(v.validate(5))  # True


# Надо понимать что, метод validate мы не можем использовать для изменения каких-либо значений
# экземпляров этого класса, поскольку в методе нет ссылки на экземпляры - self

# Используем класс-метод внутри метода init для проверки значений x, y перед их инициализацией:


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """возвращает TRUE если значение аргумента args укладывается в диапазон от MIN_COORD до
        MAX_COORD """
        return cls.MIN_COORD <= arg <= cls.MAX_COORD  # прямое обращение к св-вам класса

    def __init__(self, x, y):
        self.x = self.y = 0  # сначала обнуляем x, y
        if Vector.validate(x) and Vector.validate(y):  # а далее проверяем: если x и y проходят
            # проверку определённую в класс-методе, то ...
            self.x = x  # ...инициализируем(изменяем) x
            self.y = y  # инициализируем y
            # в противном случае x, y будут равны 0

    def validate_1(self, min_coord, max_coord):  # обычный метод объекта
        """возвращает TRUE если значение аргумента x укладывается в диапазон от min_coord до
        max_coord """
        return min_coord <= self.x <= max_coord

    def get_coords(self):
        return self.x, self.y


v = Vector(1, 2)
print(v.get_coords())  # вернёт (1, 2) поскольку значения x = 1, y = 2 прошли проверку в класс-методе

# Если же, например аргументу y присвоить недопустимое значение 200, то x и y не проинициализируются и
# останутся равными 0
v = Vector(1, 200)
print(v.get_coords())  # (0, 0)


# Но! В данном случае универсальнее производить вызов метода validate не через имя класса Vector,
# а через ссылку на текущий экземпляр класса - self, поскольку этот экземпляр так же содержит
# информацию о классе. Поэтому при использовании self интерпретатор поймёт из какого класса вызывается
# метод и подставит правильно ссылку cls в методе validate. И теперь даже если, например, изменить имя
# класса, то в самой программе ничего менять не надо. В противном случае надо было бы каждый раз менять
# синтаксис вызова метода Vector.validate на какой-либо другой

# С помощью декоратора @staticmethod мы можем определять методы, которые не имеют доступа ни к
# атрибутам класса ни к атрибутам его экземпляров. То есть создаётся некая самостоятельная независимая
# функция объявленная внутри класса
# определим внутри нашего класса статический метод, который возвращает квадратичную норму вектора:
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """возвращает TRUE если значение аргумента args укладывается в диапазон от MIN_COORD до
        MAX_COORD """
        return cls.MIN_COORD <= arg <= cls.MAX_COORD  # прямое обращение к св-вам класса

    def __init__(self, x, y):
        self.x = self.y = 0  # сначала обнуляем x, y
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    def validate_1(self, min_coord, max_coord):
        """возвращает TRUE если значение аргумента x укладывается в диапазон от min_coord до
        max_coord """
        return min_coord <= self.x <= max_coord

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        """Возвращает квадратичную норму вектора"""
        return x * x + y * y


v = Vector(1, 2)
print(v.norm2(5, 6))  # 61. Вернул квадратичную сумму вектора (5, 6)


# При этом статические методы можно вызывать и внутри обычных методов:

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """возвращает TRUE если значение аргумента args укладывается в диапазон от MIN_COORD до
        MAX_COORD """
        return cls.MIN_COORD <= arg <= cls.MAX_COORD  # прямое обращение к св-вам класса

    def __init__(self, x, y):
        self.x = self.y = 0  # сначала обнуляем x, y
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    def validate_1(self, min_coord, max_coord):
        """возвращает TRUE если значение аргумента x укладывается в диапазон от min_coord до
        max_coord """
        return min_coord <= self.x <= max_coord

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        """Возвращает квадратичную норму вектора"""
        return x * x + y * y


v = Vector(10, 20)  # 500. Вернул квадратич. норму из метода norm2 определённого в методе init

# Таким образом, подводя итог:
# из обычных методов мы можем обращаться к локальным атрибутам экземпляров, а так же к атрибутам самого
# класса MIN_COORD MAX_COORD
# из методов класса classmethod мы можем обращаться напрямую только к атрибутам самого класса
# если же нам надо определить какую-либо независимую сервисную ф-цию, которая будет работать только с
# аргументами определенными только в ней, то надо использовать статические методы staticmethod
