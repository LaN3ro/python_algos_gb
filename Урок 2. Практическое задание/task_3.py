"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""
list = input("Введите число ")
i = 0
count = len(list) - 1
new_list = []


def my_func(list, i, count, new_list):
    if count == -1:
        print(new_list)
        exit()
    new_list.insert(i, list[count])
    count -= 1
    i += 1
    my_func(list, i, count, new_list)


my_func(list, i, count, new_list)
