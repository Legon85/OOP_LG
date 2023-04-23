# ДЛЯ ТОГО ЧТОБ ПРОВЕРЯТЬ РАБОТОСПОСОБНОСТЬ НИЖЕОПИСАННОГО НЕОБХДИМО РАСКОММЕНТИРОВАТ ОТДЕЛЬНЫЕ БЛОКИ
# ПОСКОЛЬКУ ИСПОЛЬЗУЮТСЯ ФУНКЦИИ INPUT


# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print("Деление на ноль")
# except ValueError:
#     print("Ошибка типа данных")

# иногда после названия исключения можно прописывать синтаксис 'as' и какую-либо переменную,которая по сути своей будет
# являться ссылкой на объект класса исключения. В таком случае будет вместо текста определенного пользователем выводиться
# стандартное программное сообщение об исключении. Например:
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z: # z - ссылка на объект класса ZerroDivisionError
#     print(z) #  если ввести 1 0 получаем - > division by zero
# except ValueError as v: # z - ссылка на объект класса ValueError
#     print(v)  # если ввести A B получаем - > invalid literal for int() with base 10: 'A'

# на практике для обработки исключений не всегда достаточно использования try except и так же использутся finally и else
# например, если не произошло никаких ошибок, с помощью else мы можем выводить сообщение об этом:\

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print("Деление на ноль")
# except ValueError:
#     print("Ошибка типа данных")
# else:
#     print("Исключений не произошло") # если ввести например 1 2 в input

# таким образом мы получаем возможность производить какие-либо действя в блоке else только в том случае если не произошло
# никаких исключений

# в свою очередь блок finally будет выполняться всегда вне зависимости от того происходили ли какие-либо исключения:
#
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print("Деление на ноль")
# except ValueError:
#     print("Ошибка типа данных")
# finally:
#     print("Блок finally выполняется всегда") # если ввести например 1 2 в input, а если ввести 1 0,
#     # то выведется исключение division by zero но вместе с этим блок finally всё равно тоже сработает
#     # и выведет "Блок finally выполняется всегда"

# где же используется блок finally на практике - например при работе с файлами:
# педположим написан код в котором файл открыт только на чтение, но в следующей строке идёт команда
# записи в файл какой- либо информации.Это должно породить ошибку.Но! Вне зависимости от этого файл
# поосле его открытия всегда должен закрываться. Именно это и поможет сделать блок finally, поскольку
# он сработает всегда вне зависимости от того было исключение или нет
# try:
#     f = open("except_test_file.txt")
#     f.write("hello")
# except FileNotFoundError as z: # будем отлавливать ошибки типа "файл не найден"
#     print(z)
# except:
#     print("Другая ошибка") # и все остальные ошибки без разбора
# finally:
#     if f: # проверяем действительно ли был открыт файл
#         f.close() # закрываем файл
#         print("Файл закрыт") # выводим сообщение о закрытии

# ксати для замены такого функционала и был создан менеджер контекста with open as f. при его использовании не нужно
# использовать блок finally:
#
# try:
#     with open("except_test_file.txt") as f:
#         f.write("hello")
# except FileNotFoundError as z: # будем отлавливать ошибки типа "файл не найден"
#     print(z)
# except:
#     print("Другая ошибка") # и все остальные ошибки без разбора

# Так же finally может использоваться и в функциях, причём синтаксис позволяет записывать его полсе оператора return
# def get_values():
#     """ф-ция выводит введённые пользователем значения"""
#     try:
#         x, y = map(int, input().split())
#         return x, y
#     except ValueError as z:
#         print(z)
#         return 0, 0
#     finally:
#         print("finally выполнятся до return")
#
# x, y = get_values()
# print(x, y) # если ввести 1 2, то вернёт сначала сообщение "finally выполнятся до return" из блока finally а затем 1 2.
# а если ввести недопиустимые значения a b, то вернёт сначала invalid literal for int() with base 10: 'a'
# далее "finally выполнятся до return" поскольку он сработает до return, ну и далее вернёт 0 0 из блока except опять
# invalid literal for int() with base 10: 'a'
# finally выполнятся до return
# 0 0

# так же try txcept можно использовать как вложенные в уже имеющийся try except:


# try:
#     x, y = map(int, input().split())
#     try:
#         res = x / y
#     except ZeroDivisionError:
#         print("Деление на ноль")
# except ValueError as z:
#     print(z)

# вместе с этим вложенный блок try except можно вынести в отдельную ф-цию:

# def div(a, b):
#     try:
#         return = a / b
#     except ZeroDivisionError:
#         return "Деление на ноль"
#
# res = 0
# try:
#     x, y = map(int, input().split())
#     res = iv(x, y) # вызвываем ф-цию определённую выше
# except ValueError as z:
#     print(z)
#
# print(res)