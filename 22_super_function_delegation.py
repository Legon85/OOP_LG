# если имеется некий дочерний класс от класса базового с каким-либо
# прописаным методом в нём, то это называется расширением (extended) базового класса

class Geom:
    name = "Geom"


class Line(Geom):
    def draw(self): # расширение базового класса Geom
        print("рисование линнии")


# а если тот же метод drow что и в дочернем классе Line ещё и прописать
# в классе Geom, то это будет называтся переопредлением (overriding) базового класса
# напрмер:

class Geom:
    name = "Geom"

    def draw(self): # --> переопределение класса Geom классом Line
        print("рисование примитива")



class Line(Geom):
    def draw(self):
        print("рисование линнии")


# определим в базовом классе инициализатор выводящий строку "инициализатор Geom"

class Geom:
    name = "Geom"

    def __init__(self):
        print("инициализатор Geom")


class Line(Geom):
    def draw(self):
        print("рисование линнии")


l = Line()
# после установки () и запуска программы идёт следующая цепочка вызовов:
# вызывается метод __call__ (из метакласса),который в свою очередь вызывает
# метод __new__ (из базового класса obj) для создания экземпляка класса
# далее находится метод __init__ в базовом классе Geom(т.к. не находится в Line)
# ну и метод __init__ выводит искомую строку
# все эти методы изначально ищутся в классе Line и если не находятся то далее
# ищутся по цепочке иерархии базовых калассов Geom -> object -> метакласс

# a теперь определим __init__ уже в классе Line

class Geom:
    name = "Geom"

    def __init__(self):
        print("инициализатор Geom")


class Line(Geom):
    def __init__(self):
        print("инициализатор Line")

    def draw(self):
        print("рисование линнии")


l = Line() # -->  теперь выводится строка из инициализатора в классе Line

# забьём в иниц-р Line координаты:

class Geom:
    name = "Geom"

    def __init__(self):
        print("инициализатор Geom")


class Line(Geom):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("рисование линнии")


l = Line(0, 0, 10, 20)
print(l.__dict__) # ---> выводятся локальные св-ва Line: {'x1': 0, 'y1': 0, 'x2': 10, 'y2': 20}

# пропищем дополнительный класс Rect:

class Geom:
    name = "Geom"

    def __init__(self):
        print("инициализатор Geom")


class Line(Geom):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("рисование линнии")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = fill

    def draw(self):
        print("рисование прямоугольника")


l = Line(0, 0, 10, 20)
print(l.__dict__)

# в данном случае у нас происходит дублирование методов
# поэтому мы общие параметры выносим в класс Geom


class Geom:
    name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("рисование линнии")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("рисование прямоугольника")

# будут выводится иницивализаторы для разных классов
l = Line(0, 0, 10, 20) # ->  инициализатор Geom для <class '__main__.Line'>
r = Rect(1, 2 ,3, 4) # -> инициализатор Rect

# но в таком случае мы разделили метод __init__ для класса Geom и Rect,
# а значит метод __init__ найдётся в классе Rect и не пропишутся локальные св-ва x1, y1 .....
print(r.__dict__) # --> {'fill': None} нет свойств x1, x2...!!!

# чтоб можно было в инициализаторе класса Rect получать свойства из инициализатора базового класса Geom
# нужно использовать метод super(). Данный метод возвращает объект базовог класса с его свойствами
# поэтому self в скобках уже не надо прописывать см.далее:

class Geom:
    name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("рисование линнии")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2) # "делегирование". self в скобках не пишем!
        # т.к. suer() уже возвратил объект Geom
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("рисование прямоугольника")



l = Line(0, 0, 10, 20) # ->  инициализатор Geom для <class '__main__.Line'>
r = Rect(1, 2 ,3, 4) # -> инициализатор Rect

print(r.__dict__) # --> {'x1': 1, 'y1': 2, 'x2': 3, 'y2': 4, 'fill': None} теперь всё ок! св-ва на месте!

# при этом super() надо прописывать в классе Rect(Geom)  в самую первую очередь,
# иначе мы неявно переопределим свойство  self.fill см.далее:

class Geom:
    name = "Geom"

    def __init__(self ,x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = 0 # неявно меняем параметр fill базовом классе


class Line(Geom):
    def draw(self):
        print("рисование линнии")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        print("инициализатор Rect")
        self.fill = fill
        super().__init__(x1, y1, x2, y2)  # в данном случае(super() не в начале)
        # fill будет переопределятся на 0 а не на None

    def draw(self):
        print("рисование прямоугольника")



l = Line(0, 0, 10, 20) # ->  инициализатор Geom для <class '__main__.Line'>
r = Rect(1, 2 ,3, 4) # -> инициализатор Rect

print(r.__dict__) # -->{'fill': 0, 'x1': 1, 'y1': 2, 'x2': 3, 'y2': 4} fill = 0!!!!


