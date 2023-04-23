# метод __eq__ нужен для релизации сравнения секунд в виде сравнения экземпляров (с1 == с2)
# без этого метода будут сравинваться не секунды а id экземпляров(что есесственно не правильно)
class Clock:
    __Day = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be integers")
        self.seconds = seconds % self.__Day

    def __eq__(self, other):
        """переопределяет способ сравнения секунд в виде (с1 == с2)"""
        if not isinstance(other, (int, Clock)):  # проверка что входные данные явл-я int или экземпляром Clock
            raise TypeError("Операнд сппава должен иметь тип int  или Clock")

        sc = other if isinstance(other, int) else other.seconds # в sc присваиваем число если сравниваем  с числом либо секунды в экземпляре
        return self.seconds == sc # возвращаем нужный рузультат сравнения секунд
        # в операторах сравнения не имеет значения с какой стороны стоят сравниваемые элементы
        # поэтому здесь не нужны доп. методы как __radd__ для обработки таких случаев

    def __lt__(self, other):
        """определяет метод проверки на 'меньше'  <  """
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд сппава должен иметь тип int  или Clock")

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc


# c1 = Clock(1000)
# c2 = Clock(1000)
# c3 = Clock(2000)
# print(c1 == 1000) # пример сравнения секунд в случае когда они справа
# print(1000 == c2) # пример сравнения секунд в случае когда они слева
# print(c1 == c2)  # пример сравнения секунд в качестве экземпляра
# print(c1 == c3)
# print(c1 != c3) # обратить внимание, что оператор != тоже работает, не смотря на то
# # что его работу нигде не определяли. это потому, что python когда видит его интерпретирует
# # это как -> с1 != с3 эквивалентно not(c1 == c3) я с1 == с3 у нас уже определено !!!!
# print(c1 < c3) #  проверка на "меньше"

#______________________________________________________________________
# поскольку в вышеперечисленных методах есть дублирование кода можно
# реализовать рефакторинг (см.ниже)

class Clock:
    __Day = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be integers")
        self.seconds = seconds % self.__Day

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):  # проверка что входные данные явл-я int или экземпляром Clock
            raise TypeError
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __ne__(self, other):
        """ проверка на  != """
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):
        """метод для проверки <= """
        sc = self.__verify_data(other)
        return self.seconds <= sc

    # def __ge__(self, other):
    #     """метод для проверки >= """
    #     sc = self.__verify_data(other)
    #     return self.seconds >= sc


c1 = Clock(1000)
c2 = Clock(1000)
c3 = Clock(2000)
print(c1 == 1000) # пример сравнения секунд в случае когда они справа
print(1000 == c2) # пример сравнения секунд в случае когда они слева
print(c1 == c2)  # пример сравнения секунд в качестве экземпляра
print(c1 == c3)
print(c1 != c3) # обратить внимание, что оператор != тоже работает, не смотря на то
# если его работу нигде не определяли.(для проверки закоментить метод __ne__.)
# это потому, что python когда видит его интерпретирует
# это как -> с1 != с3 эквивалентно not(c1 == c3), а с1 == с3 у нас уже определено !!!!
print(c1 < c3) #  проверка на "меньше"
print(c1 > c3) # # обратить внимание, что оператор > тоже работает, не смотря на то
# если его работу нигде не определяли.(для проверки закоментить метод __gt__.)
# Это потому, что python когда видит его интерпретирует
# это как -> с1 > с3 эквивалентно c3 < c1 (меняет между собой операнды и ставит обратный знак < ),
# а c3 < c1 у нас уже определено !!!!
print(c1 <= c3) # проверка  <=
print(c1 >= c3)# # обратить внимание, что оператор >= тоже работает, не смотря на то
# если его работу нигде не определяли.(для проверки закоментить метод __ge__.)
# Это потому, что python когда видит его интерпретирует
# это как -> с1 > с3 эквивалентно c3 <= c1 (меняет между собой операнды и ставит обратный знак <= ),
# а c3 <= c1 у нас уже определено !!!!

# ВЫВОД:  для реализации методов сравнения можно определить всего 3 метода: __eq__, __lt__ и __le__,
# а остальные будут автоматически инвертированы интерпретатором