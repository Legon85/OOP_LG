# Объявить класс Point.

# Определить в нём атрибуты color = 'red' и circle = 2 класса Point

# Посредством обращения через имя класса переопределить параметр color = 'black'

# Посредством обращения через имя класса вывести параметр circle (Python console)

# Посредством обращения через имя класса вывести дандер методом коллекцию со всеми атрибутами класса Point(Python
# console).

# Создать экземпляр a класса Point(Python console).

# Создать экземпляр b класса Point(Python console).

# Вывести данные о типе объекта a

# Вывести информацию равен ли объект a классу Point (принадлежит ли ему) (Python console) методом == и  isinstance

# Посредством обращения через имя класса изменить атрибут circle = 1

# Посредством обращения через имя объекта вызвать список атрибутов объекта a дандер методом (убедиться,
# что он пустой и что изменение  атрибутов класса не влияет на атрибуты объекта т.к. они в разных пространствах имён).

# Посредством обращения через имя объекта вызвать список атрибутов объекта b дандер методом(убедиться, что он пустой и
# что изменение атрибутов класса не влияет на атрибуты объекта т.к. они в разных пространствах имён).

# Посредством обращения через имя объекта a вывести атрибут color (убедиться, что можно обращаться к атрибутам класса
# через объект

# Посредством обращения через имя объекта b вывести атрибут circle (убедиться, что можно обращаться к атрибутам класса
# через объект

# Посредством обращения через имя объекта a произвести изменение атрибута color = 'green'(убедиться, что при этом
# атрибут самого класса не поменялся, а в списке атрибутов объекта a появился новый атрибут color = 'green'

# Посредством обращения через имя класса создать новый атрибут класса type_pt = 'disc'

# Через метод setattr создать новый атрибут prop = 1  класса Point

# Через метод setattr изменить значение атрибута type_pt = 'square' класса Point.
#
# Вывести значение атрибута circle класса Point.
#
# Присвоить переменной res вывод значения атрибута circle и вывести переменную res.
#
# Посредством обращения через имя класса попробовать вывести значение несуществующего атрибута a класса Point
# (получить ошибку).
#
# С помощью метода getattr обработать ошибку вывода при обращении к несуществующему атрибуту Point и вывести в таком
# случае False
#
# С помощью метода getattr вывести существующий атрибут 'color' убедиться что просто выводит значение этого атрибута
#
# Посредством обращения через имя класса удалить атрибут 'prop' с помощью оператора del
#
# С помощью метода hasattr проверить существует ли атрибут 'prop' посредством обращения через класс Point
#
# С помощью метода hasattr проверить существует ли атрибут 'circle' посредством обращения через класс Point
#
# С помощью метода delattr удалить атрибут 'type_pt' посредством обращения через класс Point.
#
# Попробовать удалить еще раз (получить ошибку)
#
# С помощью метода hasattr проверить существует ли атрибут 'circle' посредством обращения через объект a (убедиться,
# что данный метод может обращаться к атрибутам класса через имя объекта, несмотря на то, что в пространстве имен
# этого объекта такого атрибута нет.
#
# Попробовать удалить через оператор del посредством обращения через объект a атрибут circle (убедиться, что del не
# может удалять атрибуты, отсутствующие в пространстве имен, к которому он применяется и что он не идёт удалять
# атрибут circle находящийся в пространстве имен Point).
#
# Попробовать удалить через оператор del посредством обращения через объект a атрибут color (убедиться, что атрибут
# удаляется из локальной области видимости объекта.
#
# Заново переопределить класс Point (Python console) с атрибутами color = 'red' и circle = 2.
#
# Создать объекты a и b класса Point.
#
# Присвоить объекту a собственные локальные св-ва(атрибуты) x = 1, y = 2.
#
# Присвоить объекту b собственные локальные св-ва(атрибуты) x = 10, y = 20.
#
# Прописать строку документации "Класс для представления координат точек на плоскости" в классе Point.
#
# Посредством обращения через имя класса вывести строку документации дандер методом.
