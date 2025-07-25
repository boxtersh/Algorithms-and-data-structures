import datetime

import matplotlib.pyplot as plt

# ******** classroom work **************************************************************
def __check_int(number) -> None:

    if not isinstance(number, int):

        raise TypeError('Число не класса int')


def __check_list(array: list) -> None:

    if not isinstance(array, list):
        raise TypeError(f'Не соответствие типа входных данных ожидалось class: list')


def __check_list_empty(array: list) -> None:

    if not array:
        raise ValueError(f'Список данных пустой')


def output_minimum_number_greatest_repetition(array: list[int] = None) -> int:
    """
    Функция возвращает минимальное значение из списка с максимальным количеством повторений
    Пример:
    [1,1,3,3,3,2,2,5,5,5,5] ответ 5
    [1,1,3,3,3,3,2,2,5,5,5,5] ответ 3
    [1,2,3,4] ответ 1
    [] ответ - 1
    :param array: Список целых чисел
    :return: минимальное число из списка с максимальным количеством повторений
    """
    if array is None:
        raise TypeError('Функция ожидала один обязательный элемент класса list')

    if not isinstance(array, list):
        raise TypeError('Входные данные не класса лист')

    if not array:
        return -1

    unique_number_list = [array[0]]

    for elm in array[1:]:

        if elm not in unique_number_list:
            unique_number_list.append(elm)

    if len(unique_number_list) == 1:
        return unique_number_list[0]

    dec_count = {}
    count = 0

    for elm in unique_number_list:
        for elm_1 in array:

            if elm == elm_1:
                count += 1

        dec_count[elm] = count
        count = 0

    max = dec_count[unique_number_list[0]]

    for key in unique_number_list[1:]:
        if dec_count[key] > max:
            max = dec_count[key]

    list_keys_maximum_repeated = []

    for key in unique_number_list:
        if dec_count[key] == max:
            list_keys_maximum_repeated.append(key)

    if len(list_keys_maximum_repeated) == 1:
        return list_keys_maximum_repeated[0]

    min = list_keys_maximum_repeated[0]

    for key in list_keys_maximum_repeated[1:]:
        if key < min:
            min = key

    return min


def task_N3(array: list, b: int) -> list[list]:
    """
    Функция принимает список array с ограничением длинны 2 <= array <= 104
    и значений в нем -109 <= array[i] <= 109, а так же целое число В
    с ограничением -109 <= В <= 109 и возвращает индексы уникальных комбинаций вида
    по условию array[i] + array[j] = В, i и j индексы одного уровня, но i <> j
    Пример:
    [0, 3, 0, 2, 1, 3, 0, 2, 1] B = 3
    ответ: [[0, 1], [2, 5], [3, 4], [7, 8]]

    []1,2,3,4,5] B = 7
    ответ: [[-1, -1]]
    :param array: список чисел по условию
    :return: список индексов значение чисел массива которых в сумме дает число В [i, i+n]
    """
    __check_list(array)

    if 2 > len(array) or len(array) > 104:
        raise ValueError(f'Список должен удовлетворять условию 2 <= array <= 104')

    __check_int(b)

    if -109 > b or b > 109:
        raise ValueError(f'Число B должно удовлетворять условию -109 <= В <= 109')

    mass = array.copy()
    res = []

    for i in range(len(mass)):
        for j in range(len(mass)):
            if mass[i] + mass[j] == b:
                if i != j:
                    if not [mass[i], mass[j]] in res or not [mass[j], mass[i]] in res:
                        res.append([i, j])
                        mass[i] = b + 0.1
                        mass[j] = b + 0.1

    if not res:
        res = [[-1, -1]]

    return res


# ******** Модуль №5. *********        ************         *************         ***********
# ******** Задание №1 ***********************************************************************

def factorial(n: int) -> int:
    """
    Функция возвращает факториал целого
    положительного числа n из диапазона 0 ≤ n ≤ 20
    Примет:
    5 ответ 120
    21 ответ raise
    -5 ответ raise
    2.7 ответ raise
    :param n: Число, факториал которого нужно получить
    :return: факториал числа n
    """

    __check_int(n)

    if 0 > n or n > 20:
        raise ValueError('Число не в диапазоне 0 ≤ n ≤ 20')

    if n == 0:
        return 1

    res = 1

    for elm in range(1, n + 1):
        res *= elm

    return res

# ******** Задание №2 ***********************************************************************

def fibonacci(n: int) -> list[int]:
    """
    Функция возвращает список чисел Фибоначчи
    от 0 до n-го числа (включительно)
    Пример:
    9 ответ [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    9.2 или меньше нуля ответ raise

    :param n: целое положительное
    :return: список чисел Фибоначчи
    """

    __check_int(n)

    if n < 0:
        raise ValueError('Число меньше нуля')

    if n == 0:
        return [0]

    elif n == 1:
        return [0,1]

    a, b = 0, 1
    lst_fibonacci = [a,b]

    for _ in range(n-1):
        next_number = lst_fibonacci[a] + lst_fibonacci[b]
        lst_fibonacci.append(next_number)
        a += 1
        b += 1

    return lst_fibonacci

# ******** Задание №3 ***********************************************************************

def count_ones(n: int) -> int:
    """
    Функция возвращает количество единиц в его двоичном представлении
    Пример:
    0 ответ 0
    18 ответ 10010
    -5 ответ raise ValueError
    :param n: десятичное число
    :return: двоичное представление числа n
    """

    __check_int(n)

    if n < 0:
        raise ValueError('Число меньше нуля')

    if n == 0:
        return 0

    list_bin = []

    while n > 0:
        list_bin.append(str(n % 2))
        n //= 2

    return int(''.join(list_bin[::-1]))

# ******** Задание №4 ***********************************************************************

def palindrome(x: int) -> bool:
    """
    Функция возвращает True, если x является палиндромом, и False в противном случае.
    Пример:
    123 ответ False
    12321 ответ True
    значение x не в интервале -2^31 <= x <= 2^31 - 1 ответ raise
    :param x: Целое число в интервале -2^31 <= x <= 2^31 - 1
    :return: булево значение результата
    """

    __check_int(x)

    if -2 ** 31 > x or x > 2 ** 31 - 1:
        raise ValueError('Число не в диапазоне -2^31 <= x <= 2^31 - 1')

    if x < 0:
        return False

    list_x_revers = []
    buff = x

    while x > 0:
        list_x_revers.append(x % 10)
        x //= 10

    res = 0

    for i in range(len(list_x_revers[::-1])):
        res += list_x_revers[::-1][i] * 10**i

    return res == buff

# ******** Задание №5 ***********************************************************************

with open('SQL.txt') as file:
    array = file.readlines()

dec_day = {0:'Понедельник',
           1:'Вторник',
           2:'Среда',
           3:'Четверг',
           4:'Пятница',
           5:'Суббота',
           6:'Воскресенье'}

dec_month = {1:'январь',
             2:'февраль',
             3:'март',
             4:'апрель',
             5:'май',
             6:'июнь',
             7:'июль',
             8:'август',
             9:'сентябрь',
             10:'октябрь',
             11:'ноябрь',
             12:'декабрь'}

def __transformations_to_date_visiting(array: list[str]) -> list[list]:
    """
    Функция преобразует данные из файла массива array из строки
    в список из объектов класса datatime и int
    :param array: массив строк '2023-10-15, 251'
    :return: list[[datatime, int]]
    """
    __check_list(array)

    __check_list_empty(array)

    tsf_array = []

    for row in array:
        try:
            datetime.datetime.strptime(row[:10], '%Y-%m-%d')

        except ValueError:
            raise ValueError(f'Неверный формат даты в строке: {row}, ожидалось год-месяц-дата')

        row = row.split(',')
        data = datetime.date.fromisoformat(row[0])

        if not row[1].rstrip().isdigit():
            raise ValueError(f'Неверный формат "посещения" в строке: {row}, ожидалось целое число')

        visiting = int(row[1])
        tsf_array.append([data,visiting])

    return tsf_array


def __axis_value(tsf_array: list[list]):
    """
    Функция создает два списка координат X Y. Из массива tsf_array [datatime, int]
    получаем список посещений [int] - координата Y  и список [int] (порядковые номера дат) координата Х
    :param tsf_array: list[[datatime, int]]
    :return: Два списка [int]
    """
    lst_data = [1]
    lst_visiting = [tsf_array[0][1]]
    i = 2

    for row in tsf_array[1:]:
        lst_data.append(i)
        lst_visiting.append(row[1])
        i += 1

    return lst_data, lst_visiting


def __max_visiting_to_month(tsf_array: list[list]):
    """
    Функция создает из массива tsf_array словарь
    данных - месяц (ключ) сумма посещений за месяц (значение)
    и максимум посещений за все месяцы
    Пример:
    [[2023-01-01,150], [2023-01-02,200], [2023-01-03,250]]
    ответ {1: 600}, 750
    :param tsf_array: list[[datatime, int]]
    :return: словарь и максимум посещений за все месяцы
    """

    max_visiting = tsf_array[0][1]
    dec_sum_month = {}
    sum = 0

    for month in dec_month.keys():
        for i in range(len(tsf_array)):

            if tsf_array[i][0].month == month:
                sum += tsf_array[i][1]

        if max_visiting < sum:
            max_visiting = sum

        if sum > 0:
            dec_sum_month[month] = sum

        sum = 0

    return dec_sum_month, max_visiting


def __max_visiting_to_day(tsf_array: list[list]):
    """
    Функция создает из массива tsf_array словарь
    данных - день недели (ключ) сумма посещений за аналогичные дни (значение)
    и максимум от суммы посещений за аналогичные дни - за весь период
    Пример:
    [[2023-01-01,150], [2023-01-02,200], [2023-01-03,250]]
    все понедельники - 613, вторники - 543, среды - 750 ... максимум = 750
    ответ {0: 613, 1: 543, 2: 750}, 750
    :param tsf_array: list[[datatime, int]]
    :return: словарь и максимум посещений за день за весь период
    """
    max_visiting = tsf_array[0][1]
    dec_sum_day = {}
    sum = 0

    for day in dec_day.keys():
        for i in range(len(tsf_array)):

            if tsf_array[i][0].weekday() == day:
                sum += tsf_array[i][1]

        if max_visiting < sum:
            max_visiting = sum

        if sum > 0:
            dec_sum_day[day] = sum

        sum = 0

    return dec_sum_day, max_visiting


def display_visiting_to_month(tsf_array: list[list]) -> None:
    """
    Функция из массива tsf_array выводит на экран упорядочный
    словарь по убыванию посещений сайта по месяцам
    Пример:
    январь       - 6630,   100% от максимума
    февраль      - 6543,    99% от максимума
    :param tsf_array: list[[datatime, int]]
    """

    dec_sum_month, max_visiting = __max_visiting_to_month(tsf_array)
    dec_sum_month = dict(sorted(dec_sum_month.items(), key=lambda value: value[1], reverse=True))

    for key in dec_sum_month.keys():
        print(f'{dec_month[key]:12} - {dec_sum_month[key]}, {round(100*dec_sum_month[key]/max_visiting):5}% от максимума')


def display_visiting_to_day(tsf_array: list[list]) -> None:
    """
    Функция из массива tsf_array выводит на экран упорядочный
    словарь по убыванию посещений сайта по дням недели
    Пример:
    Воскресенье  - 2130,   100% от максимума
    Вторник      - 2013,    95% от максимума
    Понедельник  - 2000,    94% от максимума
    Суббота      - 1910,    90% от максимума
    Пятница      - 1840,    86% от максимума
    Четверг      - 1790,    84% от максимума
    Среда        - 1490,    70% от максимума
    :param tsf_array: list[[datatime, int]]
    """
    dec_sum_day, max_visiting = __max_visiting_to_day(tsf_array)
    dec_sum_day = dict(sorted(dec_sum_day.items(), key=lambda value: value[1], reverse=True))

    for key in dec_sum_day.keys():
        print(f'{dec_day[key]:12} - {dec_sum_day[key]}, {round(100*dec_sum_day[key]/max_visiting):5}% от максимума')


def data_graph(array) -> None:
    """
    Функция из массива выводит на экран
    график посещений сайта по дням за весь период для удобной визуализации
    :param tsf_array: list[[datatime, int]]
    """

    tsf_array = __transformations_to_date_visiting(array)
    lst_data, lst_visiting = __axis_value(tsf_array)

    x = lst_data
    y = lst_visiting

    plt.figure(figsize=(13, 6))
    plt.plot(x, y, label='Посещение')
    plt.title('График посещения сайта')
    plt.xlabel('Дата')
    plt.ylabel('Посещения')
    plt.grid(True)
    plt.legend()
    plt.show()