class FRange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        """ по сути этот метод релизует итерирование по элементам range
        и возращает текущее значение последовательности"""
        if self.value + self.step < self.stop: # проверка что следующий итер-ый объект не выходит за рамки range
            self.value += self.step # новый шаг итерации
            return self.value # воpзвращаем текущее значение итерации
        else:
            raise StopIteration


fr = FRange(0, 2, 0.5)
# print(fr.__next__()) # -> 0.0
# print(fr.__next__()) # -> 0.5
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__()) # -> StopIteration except
# но теперь всё тоже самое можно прописать через обычную ф-цию next -> next(fr)
# print(next(fr)) # -> 0.0
# print(next(fr)) # -> 0.5
# print(next(fr))
# print(next(fr))
# print(next(fr)) # -> StopIteration except

# но на данном этапе мы не можем воспользоваться циклом for для объекта fr
# т.к. сейчас объект не является итерируемым и к нему не может быть применена ф-ция it = iter(fr)
# чтобы сделать его итерируемым надо так же прописать метод __iter__  далее...


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start
        self.stop = stop
        self.step = step


    def __next__(self):
        """ по сути этот метод реализует итерирование по элементам range
        и возращает текущее значение последовательности"""
        if self.value + self.step < self.stop: # проверка что следующий итер-ый объект не выходит за рамки range
            self.value += self.step # новый шаг итерации
            return self.value # вывод текущего значения итерации
        else:
            raise StopIteration

    def __iter__(self):
        """метод по сути всего лишь возвращает нам объект т.к. сам объект уже
         является итератором и нужно это для автоматизации итерирования
         в циклах for например (без этого метода можно лишь вручную каждый раз
         вызывать метод __next__) в отличии от ф-ции iter где уже встроено и
         итерирование и его автоматическое вызывание в циклах"""
        self.value = self.start - self.step # в данном случае value можно определить в этом методе
        return self


fr = FRange(0, 2, 0.5)
it = iter(fr)
print(list(it))
# for x in fr:
#     print(x) # теперь цикл for работает исправно


# пример использования с 2мя циклами (один вложенный) для вывода нескольких(заданных) строк одного цикла
# со списком проитерированых значений второго цикла:

class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=0.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step) # класс FRange(описан выше) формирует числа для каждой строки rows

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = FRange2D(0, 2, 0.5, 4)
for row in fr: # проходимся во внеш цикле по итератору объекта класа FRange2D(по 4ём строкам)
    for x in row: # в каждой строке проходимся по итератору класса Frange( по числам range)
        print(x, end=" ")
    print() #  получаем таблицу строк состоящих из чисел генератора