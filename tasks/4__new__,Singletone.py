# В классе Point последовательно определить методы __new__ и __init__
#
# В методе new определить распечатывание строки: Вызов __new__ для + строчная ссылка на текущий класс.
#
# В методе init определить распечатывание строки: Вызов __init__ для + строчная ссылка на экземпляр,
# а так же формирование локальных св-в экземпляров x и y задаваемых формально и по умолчанию равными 0.
#
# Создать объект pt с x=1 и y=2
#
# Запустить программу и убедиться что сработал только метод new, но объект создан не был, распечатав для этого объект
# pt.
#
# Дописать метод new так, чтобы он возвращал как полагается адрес нового созданного объекта.
#
# Снова запустить программу и убедиться что сработали оба метода и объект был создан с нужными свойствами.
#
# Попробовать убрать из списка аргументов метода new аргументы *args и **kwargs и запустив программу получить ошибку.
#
# Ответить на вопрос зачем нужны эти аргументы и что в них передаётся.
#
# Определить класс DataBase для пояснения паттерна SINGLETON
#
# Метод init этого класса определяет следующие локальные свойства: user, psw, port.
#
# Метод connect распечатывает: соединение с БД: ссылка на user, ссылка на psw, ссылка на port.
#
# Метод close печатает: закрытие соединения с БД.
#
# Метод read печатает: данные из БД.
#
# Метод write печатает: запись в БД data (data принимает на вход)
#
# В качестве свойства класса объявить переменную _instance равную None.
#
# Переопределить метод new в контексте SINGLETON, так, что бы он создавал новый объект только в том случае если
# _instance равно None. Ну а в противном случае чтоб возвращал ссылку на уже существующий объект.
#
# Так же определить метод __del__ который в случае удаления объекта будет присваивать _instance обратно значение None.
#
# Создать экземпляр класса db co свойствами ('root', '1234', 80).
#
# Создать ещё один экземпляр db2  ('root2', '5678', 40).
#
# Вывести id обоих объектов и убедиться, что они одинаковые. То есть нового объекта не создалось.
#
# Но! Показать что ввиду не переопределенного метода  __cal__ свойства объекта поменяются на свойства второго
# объекта. Для этого вызвать метод connect.
#
#
#