class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self): # getter для обращения к приватному св-ву __old
        return self.__old

    def set_old(self, old): # setter для установки новых значений св-ву __old
        self.__old = old


p = Person("Andrey", 20)
p.set_old(35) # через setter изменяем возраст объекта на 35
print(p.get_old()) # через getter выводим возраст объекта


# но при таком варианте как описано выше нам необходимо прописывать setter и getter для каждого приватного св-ва
# например для __name нужно будет снова писать setter и getter,что на самом деле не практично и неудобно
# свойство @Property как раз испольлзуется для решения этой проблемы
# для этого в имеющемся уже классе прописывается ещё одно св-во,например old, которое будет являться по сути
# объектом класса property, а класс property будет принимать в качестве аргументов get_old и set_old.
# Тем самым при вызове св-ва old через экземпляр: print(p.old) будет автоматически срабатывать метод get_old,
# а при записи p.old = 35 будет вызываться метод set_old

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self): # getter для обращения к приватному св-ву __old
        return self.__old

    def set_old(self, old): # setter для установки новых значений св-ву __old
        self.__old = old

    old = property(get_old, set_old) # добавляем св-во property

p = Person("Andrey", 20)
print(p.old) # -> 20  прочитали значение возраста
p.old = 45 # изменили значение возраста
print(p.old, p.__dict__) # -> 45 {'_Person__name': 'Andrey', '_Person__old': 45}

# надо заметить, что при наличии св-ва property (old) в классе, при присвоении нового значени (p.old = 45 например)
# не создаётся какое-то новое св-во old текущего класса (что по идее, по сиктаксису должно было бы происходить),
# потому, что в данном случае св-во old property находится в приоритете по выполнению

# но на текущий момент в нашей реализации есть функциональное дублирование: мы можем работать с приватным св-вом __old
# и через property и через setter и getter
# класс property имеет в себе декораторы (функции, которые расширяют функционал другой функции)
# setter(), getter() и deleter()
# и тогда вместо записи old = property(get_old, set_old) можно прописать вызовы методов set_old и get_old
# через декораторы класса property (setter и getter), а именно: old = old.setter(set_old) и old = old.getter(get_old)


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self): # getter для обращения к приватному св-ву __old
        return self.__old

    def set_old(self, old): # setter для установки новых значений св-ву __old
        self.__old = old

    old = property()
    old = old.getter(get_old)
    old = old.setter(set_old)  # переписали с помощью декораторов



p = Person("Andrey", 20)
print(p.old) # -> 20  прочитали значение возраста
p.old = 45 # изменили значение возраста
print(p.old, p.__dict__)


# теперь произведём запись того же что и выше, но в более правильном варианте:

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property  # пропсывается обязательно над get_old!!!!
    def get_old(self): # здесь уже get_old становится объектом property
        return self.__old

    @get_old.setter # через объект get_old вызываем setter
    def get_old(self, old): # set_old меняем на get_old чтоб всё функционально правильно работало
        self.__old = old

    # old = property()
    # old = old.getter(get_old)
    # old = old.setter(set_old)  # переписали с помощью декораторов



p = Person("Andrey", 20)
print(p.get_old) # -> 20  прочитали значение возраста
p.get_old = 45 # изменили значение возраста
print(p.get_old, p.__dict__)

# а теперь чтоб не было визуальной путаницы все методы и декораторы в классе можно назвать обратно old
# ну и добавим deleter  в класс

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property  # пропсывается обязательно над get_old!!!!
    def old(self): # переименовывем get_old в old
        return self.__old

    @old.setter # переименовывем get_old в old
    def old(self, old): # переименовывем get_old в old
        self.__old = old

    @old.deleter # прописывается для удаления локального св-ва объектов
    def old(self):
        del self.__old

p = Person("Andrey", 20)
del p.old # удаляем локальное св-во old из объекта
print(p.__dict__) # -> {'_Person__name': 'Andrey'} видим, что св-во  __old удалено