class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)



s1 = Student("Sergey" ,[5, 5, 3, 2, 5])
print(s1.marks[2])

# что если мы хотим для запроса оценки использовать не print(s1.marks[2],
# a синтаксис следующего вида:print(s1[2]) - испльзовать  __getitem__


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        """метод получает в качестве аргумента
        номер елемента итерируемого объекта и выводт
        элемент под этим номером """
        return self.marks[item]



s1 = Student("Sergey" ,[5, 5, 3, 2, 5])
print(s1[2])  # теперь синтаксис работает и получаем тоже 3
# метод работает с любым итерируемым объектом
# принятым в качестве аргумента в методе __init__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        return self.name[item]


s1 = Student("Sergey" ,[5, 5, 3, 2, 5])
print(s1[2]) # теперь получили 2ой элементе имени "Sergey"

# можно дооформить метод чтоб он
# выводил инф-ю об ощибке если ввели неверный индекс:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        raise IndexError("Не верный индекс")


s1 = Student("Sergey" ,[5, 5, 3, 2, 5])
# print(s1[20])  # получаем обработану ошибку Неверный индекс(роскомент для проверки)

#-------------------------------------------------------------
# для того чтоб иметь возможность менять оценки по такому же принципу: s1[2] = 4
# нужно использовать метод __setitem__


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        raise IndexError("Не верный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0: # проверка значения индекса на валидность
            raise TypeError("Индекс списка должен быть целым неотрицательным числом")
        self.marks[key] = value # меняет значение указанного элемента

s1 = Student("Sergey" ,[5, 5, 3, 2, 5])
s1[2] = 4
print(s1[2]) # выводим измененное значение 4

# чтоб мы могли при наборе синтаксиса s1[6] = 4 (индекс 6 превышает длину списка) не получать ощибку,
# а просто создавать новый элемент с указанным индексом
# нужно прописать специальный блок реализующий такой функционал

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        raise IndexError("Не верный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс списка должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks) # тут вычисляется кол-во эл-ов необходимых
            # для увеличения списка до нужного индекса
            self.marks.extend([None]*off) # непосредственно увеличиваем список на высчитаное кол-во off
        self.marks[key] = value


s1 = Student("Sergey" ,[5, 5, 3, 2, 5])
s1[10] = 4
print(s1.marks, s1[10])

#--------------------------------------------------------------
# чтоб удалять элементы по тому же принципу прописываем метод __delitem__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        raise IndexError("Не верный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс списка должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс списка должен быть целым неотрицательным числом")

        del self.marks[key]


s1 = Student("Sergey" ,[5, 5, 3, 2, 5])
del s1[2] # удаляем элемент с инд 2
print(s1.marks)