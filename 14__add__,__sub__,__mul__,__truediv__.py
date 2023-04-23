class Clock:
    __Day = 86400  # число секнд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be integers")
        self.seconds = seconds % self.__Day # остаток от деления на секунд в одном дне(чтоб не выходить за это значение)

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        """используется для реализации прибавления значений
        непосредственно к экземляру в виде -> c1 = c1 + 100"""
        if not isinstance(other, (int, Clock)): # проверка на валидность типа вводимых данных (int) либо Clock
            raise ArithmeticError ("the right operand must be an integer")

        # нижеприводимый блок нужен для реализации возможности использовать в качестве
        # прибавляемой переменной сами экземпляры ( в данном примере - с2)
        sc = other # объявляем вспомогательную переменную
        if isinstance(other, Clock):  # проверяем что other является объектом(экземпляром) Clock
            sc = other.seconds # присваиваем вспом.переменной числовое значение секунд

        return Clock(self.seconds + sc)  # прибавляем к аргументу класса наше значение


    def __radd__(self, other):
        """Данный метод используется для случаев когда прибавляемое число
        записали слева от экземпляра(100 + c1) и он всего лишь переопределяет
        порядок действий в нужное русло!!!"""
        return self + other # по сути тут просто меняются местами входные данные (c1 и 100)

    def __iadd__(self, other):
        """ метод нужен для реализации операнда += поскольку без этого метода
        будет не просто изменяться локальное свойство seconds, а будет
        создаваться новый экземпляр при операции c1 += 100"""
        # print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("the right operand must be an integer")

        sc = other # объявляем вспомогательную переменную
        if isinstance(other, Clock):  # проверяем что other является Clock
            sc = other.seconds # присваиваем вспом.переменной числовое значение секунд

        self.seconds += sc # изменяем seconds на нужное нам число sc
        return self


c1 = Clock(1000)
print(c1)
# c1.seconds = c1.seconds + 100  # в данном случае сработала обыная схема прибавления к свойству экземпляра
c1 = c1 + 100  # в данном вызове срабатывает метод экземпляра __add__ что и позволяет использовать констукцию
print(c1)
print(c1.get_time())

# c1 = Clock(1000)
# c2 = Clock(2000)
# c3 = c1 + c2
# print(c3.get_time())  # пример использования экземпляра в качестве вротого аргумента для прибавления секунд

# c1 = Clock(1000)
# c2 = Clock(2000)
# c3 = Clock(3000)
# c4 = c1 + c2 + c3 # при каждой операции сложения (c1+с2) образуется временная переменная(допустим t1)
# # и далее эта временная переменная складывается последовательно с с3 и удаляется сборщиком мусора и т.д.
# print(c4.get_time())
#
# c1 = Clock(1000)
# c1 = 100 + c1
# print(c1.get_time()) # пример работы метода __radd__
#
c1 = Clock(1000)
print(c1)
c1 += 100
print(c1)
print(c1.get_time()) # пример работы __iadd__