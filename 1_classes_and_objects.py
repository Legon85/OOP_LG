# простейшее определение класса
class Point:
    pass


# Добавим переменные внутри класса (называют атрибутами или свойствами класса)


class Point:
    color = 'red'
    circle = 2


#  способы обращения к переменныv
print(Point.color)  # -> red
# чтоб перезаписать св-во:
Point.color = "black"
print(Point.color)  # -> black

# для просмотра всех св-тв используется __dict__:
print(Point.__dict__)  # -> {'__module__': '__main__', 'color': 'black', 'circle': 2,
# '__dict__': <attribute '__dict__' of 'Point' objects>,
# '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}

# создадим объект(экземпляр) класса:
a = Point()
b = Point()

# явно определить, что переменные a, b ссылаются на объекты класса Point можно следующими способами:
print(type(a))  # <class '__main__.Point'>
print(type(a) == Point)  # True
print(isinstance(a, Point))  # True

# объекты a, b сейчас не содержат никаких атрибутов. Чтоб посмотреть исп. dict:
print(a.__dict__)  # {}
print(b.__dict__)  # {}

# но обращаться к св-вам класса можно:
print(a.color)  # black

# но изменять объектом св-ва класса нельзя. При попытке изменения мы лишь создадим собственное св-во
# объекта:
a.color = 'green'
print(a.color)
print(a.__dict__)  # {'color': 'green'} создалось св-вj объекта

