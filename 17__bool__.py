class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(bool(p))  # в данном случае bool всегда будет возвращать True для любых объектов класса

# но данное поведение можно переопределить с помощью __len__ или __bool__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        """данный метод за чтё возвращения определённого результата
        (либо действительного либо пустого) переопределяет поведение
        функции bool т.к. она в зависимости от этих рузльтов будет
        вазвращать уже либо True либо False"""
        # print("__len__")
        return self.x * self.x + self.y * self.y


p = Point(3, 4)
print(len(p))
print(bool(p)) #  возвращает нам True поскольку рузультат метода len = 25(действительный)
p1 = Point(0, 0)
print(len(p1))
print(bool(p1)) #  возвращает нам False поскольку рузультат метода len = 0(пуст)

# но если в классе определить метод __bool__ то для определения булевых значений будет поумолчанию
# вызываться именно он пример:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        # print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        """в данном примере __bool__ будет возвращать
        True если коорд.x == коорд.y"""
        # print("__bool__")
        return self.x == self.y # задаём условие по которому будет отрабатывать __bool__


p = Point(10, 10)
print((bool(p))) # возпращает True т.к. x == y
p1 = Point(1, 10)
print(bool(p1)) # возвр False т.к. x != y

# но в вышеописанном явном варианте __bool__ как правило не исп-ся

# пример как можно использовать этот метод в неявном формате

p = Point(1, 10)
if p: # здесь неявно вызывается метод __bool__
    print("объект p дает True")
else:
    print("объект p дает False")




p = Point(10 , 10)
if p: # здесь неявно вызывается метод __bool__
    print("объект p дает True")
else:
    print("объект p дает False")




