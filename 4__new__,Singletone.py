# метод __new__ вызывается непосредственно перед созданием объекта класса и принимает в качестве
# первого обязательного параметра ссылку на сам класс - cls.
class Point:
    def __new__(cls, *args, **kwargs):
        print(f"вызов __new__ для {cls}")

    def __init__(self, x=0, y=0):
        print(f"вызов __init__ для {self}")
        self.x = x
        self.y = y


# Если создать экземпляр и запустить программу в таком виде, то сработает метод new и распечатает:
# вызов __new__ для <class '__main__.Point'>. Но при этом не создастся объект. Чтоб создавались объекты
# метод new должен возвращать ссылку на объект, которую при этом он берёт из базового класса, стоящего
# выше по иерархии, посредством вызова метода super() и __new__ базового класса
pt = Point(1, 2)


# print(pt)

class Point:
    def __new__(cls, *args, **kwargs):
        print(f"вызов __new__ для {cls}")
        return super().__new__(cls)  # вызов new базового класса object

    def __init__(self, x=0, y=0):
        print(f"вызов __init__ для {self}")
        self.x = x
        self.y = y


pt = Point(1, 2)  # эти аргументы в скобках как раз и передаются автоматически в аргументы *args **kwargs
# метода __new__

print(pt)


# получим в выводе:
# вызов __new__ для <class '__main__.Point'>
# вызов __init__ для <__main__.Point object at 0x000002071C217DC0>
# <__main__.Point object at 0x000002071C217DC0>

# Суть и необходимость существования метода __new__ можно продемонстрировать на паттерне проектирования
# SINGLETON. Суть паттерна состоит в том, чтобы создать состояние при котором в программе мог бы
# существовать только 1 объект в один момент времени. То есть если у нас, к примеру, есть класс
# DataBase и мы создали его экземпляр db = DataBase(). То при попытке создания ещё одного экземпляра,
# db2 = DataBase(), новый экземпляр создаваться не будет. А переменная db2 будет ссылатьcя всё на тот же
# экземпляр db

class DataBase:
    __instance = None  # создаём контрольную переменную для определения существует ли уже экземпляр(она
    # будет хранить ссылку на экземпляр если он уже существует

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  # если экземпляра не существует...
            cls.__instance = super().__new__(cls)  # ..то создаём новый экземпляр обычным способ
            # метода new и присваиваем ссылку на него переменной __instance

        return cls.__instance  # в противном случае возвращаем ссылку на уже существующий экземпляр

    def __del__(self): # определяем метод del что бы, в случае удаления объекта, переменная __instance
        # снова становилась None и можно было создавать новый объект
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print("закрытие соединения в БД")

    def write(self, data):
        print(f"запись в БД{data}")


db = DataBase('root', '1234', '80')
db2 = DataBase('root2', '5678', '40')
# после попытки создания 2х объектов выводим их id и убеждаемся, что никакого 2го объекта не было создано
# и выводится один и тот же id для обеих переменных db и db2
print(id(db), id(db2))  # 1291991841520 1291991841520


# Единственный ньюанс в нашем текущем коде в том, что если вызвать у объектов db и db2 методы connect()
# то во втором выводе(для переменной db2) мы получим данные определённые для этого экземпляра:
db.connect()  # соединение с БД: root2, 5678, 40
db2.connect()  # соединение с БД: root2, 5678, 40
# Что очевидно не совсем то что мы ожидали. Происходит это потому, что даже несмотря на то, что создаётся
# один экземпляр, инициализатор __init__ всё равно каждый раз обновляет локальные св-ва.
# Но об этом в другой раз ) а на данном этапе хватит просто объяснения принципа создания единственного
# оъекта SINGLETONE