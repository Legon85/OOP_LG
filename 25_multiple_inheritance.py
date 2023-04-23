# множественное наследование (то есть дочернего класса от нескольких базовых)
class Goods:
    def __init__(self, name, weight, price):
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class NoteBook(Goods):
    pass


n = NoteBook("Acer", 1.5, 30000)
n.print_info()

# предположим нам надо добавить в функционал программы логирование товаров. Вместо того чтоб добавлять его
# в базовый класс или класс иерархией выше правильнее добавить его в отдельный калсс, напр. MixinLog:

class Goods:
    def __init__(self, name, weight, price):
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog: # добавление класса для логирования товара с использованием их ID
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class NoteBook(Goods, MixinLog): # добавляем к дочернему классу ещё один базвый  MixingLog(множеств.наслед)
    pass


n = NoteBook("Acer", 1.5, 30000)
n.print_info()
# n.save_sell_log()

# пробуем вызвать метод save_sell_log второго базового класса из оъекта NoteBook, но получим ошибку(раскоментир.для проверки)
# т.к. не был найден атрибут id потому, что в цепочке вызовов (NoteBook->Goods->MixinLog)
# отработал только инициализатор __init__ базового класса Goods и на этом всё завершилось
# чтоб такой ошибки не было надо прописывать делегирование super() в каждом классе в цепочке:

class Goods:
    def __init__(self, name, weight, price):
        super().__init__() # делегируем вызов инициализатора далее (классу MixinLog)
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog: # добавление класса для логирования товара с использованием их ID
    ID = 0

    def __init__(self): # после делегирования инициализатор этого класса будет срабатывать
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class NoteBook(Goods, MixinLog): # добавляем к дочернему классу ещё один базвый  MixingLog(множеств.наслед)
    pass


n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log() # теперь метод класса MixiLog отрабатывает -> 1: товар был продан в 00:00 часов

# сушествует специальный алгоритм обхода базовых классов при запрашиваемых из них атрибутах, методах например
# называется MRO - Method Resolution Order и соответствует их порядку записанному в скобках дочернего класса
# в нашем случае это: (NoteBook -> Goods -> MixinLog -> object) object это встроенный класс Python обходится
# всегда в конце
# цепочку MRO можно посмотреть с помощью спец.метода __mro__:

print(NoteBook.__mro__) #-> (<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>, <class 'object'>)

# важно понимать, что базовый класс, инициализатор которого должен срабатывать обязательно в первую очередь
# надо прописывать всегда первым. в противном случае объекты не будут получать необходимые им атрибуты
# в нашем случае это -> Acer, 1.5, 30000

# если для прмера поменять порядок базовых классов местами,то получим ошибку:

class Goods:
    def __init__(self, name, weight, price):
        super().__init__() # делегируем вызов инициализатора далее (классу MixinLog)
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog: # добавление класса для логирования товара с использованием их ID
    ID = 0

    def __init__(self): # после делегирования инициализатор этого класса будет срабатывать
        # -> MixinLog.__init__() takes 1 positional argument but 4 were given
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class NoteBook(MixinLog, Goods): # поменяли местами базовые классы - получили ошибку!!!
    pass

#
# n = NoteBook("Acer", 1.5, 30000) # раскоментировать, чтоб проверить!!!
# n.print_info()
# n.save_sell_log()

# при формировании множественного наследования нужно продумывать запись базовых классов так,
# чтоб все последующие после первого класса базовые калссы не нуждались ни в каких дополнительных
# параметрах кроме self. в противном сулчае могут возникнуть турдности!!!! например:

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self, p1): # добавили ещё один параметр - получили ошибку!!! ->
        # TypeError: MixinLog.__init__() missing 1 required positional argument: 'p1'
        # поскольку этот параметр в таком случае надо было прописывать и в объекте super() (в классе Goods)
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class NoteBook(Goods, MixinLog):
    pass


# n = NoteBook("Acer", 1.5, 30000)
# n.print_info()
# n.save_sell_log()  #Раскоммент. для проверки!!

# теперь пропишем в super() необходимый параметр :

class Goods:
    def __init__(self, name, weight, price):
        super().__init__(1) # прописываем требуемый параметр - ошибок нет
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self, p1): # теперь ошибок нет т.к. прописали p1 в super() класса Goods
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class NoteBook(Goods, MixinLog):
    pass

n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log()


# но что если у нас не один класс MixinLog? :

class Goods:
    def __init__(self, name, weight, price):
        super().__init__(1) # прописываем требуемый параметр - ошибок нет
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self, p1):
        super().__init__(1, 2) # делегируем очередь классу MixinLog2 и передаём параметры - ошибок нет
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class MixinLog2:
    def __init__(self, p1, p2):
        print("init MixinLog 2")


class NoteBook(Goods, MixinLog, MixinLog2): # добавляем класс MixinLog2 в очередь
    pass

n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log() # -> 1: товар был продан в 00:00 часов   ошибок нет

# Но !!! Нужно обратить внимание, что если программист не знает порядок прописывания классов в очереди и например
# и перепутает MixinLog с MixinLog2 (а это на самом деле не так и очевидно), то будет ошибка !!! :

class Goods:
    def __init__(self, name, weight, price):
        super().__init__(1) # прописываем требуемый параметр - ошибок нет
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self, p1):
        super().__init__(1, 2) # делегируем очередь классу MixinLog2 и передаём параметры - ошибок нет
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class MixinLog2:
    def __init__(self, p1, p2):
        super().__init__()
        print("init MixinLog 2")


class NoteBook(Goods,  MixinLog2, MixinLog): # очередь перепутана - будет ошибка
    pass

# n = NoteBook("Acer", 1.5, 30000)
# n.print_info()
# n.save_sell_log() # раскоммент для проверки
# получаем ошибку  -> MixinLog2.__init__() missing 1 required positional argument: 'p2'

# именно поэтому во всех базовых калссах кроме первого (с инициализацией основных праметров) не
# рекомендуется использовать дополнительные параметры. И, если мы будем исппользовать только
# self в этих калссах, то ошибок не будет возникать даже если калссы будут записаны не по проядку:


class Goods:
    def __init__(self, name, weight, price):
        super().__init__() # прописываем требуемый параметр - ошибок нет
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__() # делегируем очередь классу MixinLog2 и передаём параметры - ошибок нет
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class MixinLog2:
    def __init__(self):
        super().__init__()
        print("init MixinLog 2")


class NoteBook(Goods,  MixinLog2, MixinLog): # очередь перепутана - но теперь ошибки не будет
    pass
n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log() # -> теперь всё работает, хотя классы и записаны не в том порядке что изначально
print(NoteBook.__mro__) # -> <class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog2'>, <class '__main__.MixinLog'>, <class 'object'>

# далее рассмотрим ситуации с вызовом методов с одинаковыми именами в базовых калссах:
# скопируем метод print_info в класс MixinLog

class Goods:
    def __init__(self, name, weight, price):
        super().__init__() # прописываем требуемый параметр - ошибок нет
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

    def print_info(self):
        print("print_info из MixinLog")


class NoteBook(Goods, MixinLog):
    pass
n = NoteBook("Acer", 1.5, 30000)
n.print_info()  # -> в данном случае призойдёт вызов print_info класса Goods
# но! если мы хотим вызывать print_info именно из класса MixinLog, то нужно явно указать из какого класса
# мы вызываем нужный метод и в качестве аргумента передать ссылку на объект класса NoteBook - n:
MixinLog.print_info(n) # -> print_info из MixinLog

# но если мы хотим,чтобы print_info всегда вызывался поумолчанию из класса MixinLog, то нужно переопределить это
# в классе NoteBook след. образом:

class Goods:
    def __init__(self, name, weight, price):
        super().__init__() # прописываем требуемый параметр - ошибок нет
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

    def print_info(self):
        print("print_info из MixinLog")


class NoteBook(Goods, MixinLog):
   def print_info(self): # определяем вызов print_info из класса MixinLog в самом классе NoteBook
       MixinLog.print_info(self)

n = NoteBook("Acer", 1.5, 30000)
n.print_info() # -> print_info из MixinLog