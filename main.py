# ******** classroom work **************************************************************

def output_minimum_number_greatest_repetition(array: list[int]) -> int:
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