class Cat:
    def __init__(self, name):
        self.name = name


cat = Cat('Vaska')
print(cat)  # -> <__main__.Cat object at 0x0000027C90CFBFD0>


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """ используется для переопределения и
        отображения информации в другом виде
        и применяется для вывода отладочной инф. программисту"""
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        """ используется для переопределения и
        отображения информации в другом виде,
        но в данном случае для обычного пользо-
        вателя
        """
        return f'{self.name}'

cat = Cat('Vaska')
cat #  если в консоли напечатать cat сработает метод __repr__ -> <class '__main__.Cat'>: Vaska
print(cat) # теперь, если напечатать print(cat) или str(cat) инофрмация выводится по другому -> Vaska


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        """ определяет метод вывода длины входных данных экземпляра  """
        return len(self.__coords)

    def __abs__(self):
        """ определяет метод вывода модуля входных данных экземпляра  """
        return list(map(abs, self.__coords))

p = Point(1, -2, -5)  # в данном случае входные данные это список [1, -2, -5]
print(len(p))  # с помощью метода __len__ получили возможность вывода длины входных данных
print(abs(p))




