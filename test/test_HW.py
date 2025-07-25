import pytest
import datetime
import main

@pytest.mark.parametrize('lst, expected',
                           [([], -1),
                            ([1,1,2,2,3,3,4,4,4], 4),
                            ([-1,-1,2,2,3,3,4,4], -1),
                            ([1,1,1,1,1,1,1,1], 1),
                            ([-1,-1,-1,-1,-1,-1,-1,-1], -1),
                            ([1,2,3,4,5,6,7,8], 1),
                            ([9,4,7,1,5,3,5,9,2,8], 5)])

def test_output_minimum_number_greatest_repetition(lst, expected):

    res = main.output_minimum_number_greatest_repetition(lst)

    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_type_date_not_list():

    with pytest.raises(TypeError):
        main.output_minimum_number_greatest_repetition('')


def test_function_without_arguments():

    with pytest.raises(TypeError):
        main.output_minimum_number_greatest_repetition()


# ******** Задание №3 из презентации ********************************************************

@pytest.mark.parametrize('mass, b, expected',[([1,2,3,4,5,6], 7, [[0,5], [1,4], [2,3]]),
                                              ([-1,-2,-3,0,-5,1], 7, [[-1, -1]]),
                                              ([3,3,3,3,3,3,3], 6, [[0,1], [2,3], [4,5]]),
                                              ([0,-3,0,2,1,3,0,2,-1], 1, [[0,4], [3,8]]),
                                              ([-1,-3,-2,-2,-1,-3,-3,2,-1], 5, [[-1, -1]]),
                                              ([-109, 0, 109, 0], 109, [[1, 2]]),
                                              ([-109, 0, -109, 0], -109, [[0, 1], [2, 3]]),
                                              ([1,2,3,4,5,6], 13, [[-1, -1]])])

def test_task_N3(mass, b, expected):

    res = main.task_N3(mass, b)

    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_task_N3_argument_not_list():

    with pytest.raises(TypeError):
        main.task_N3('', -250)


def test_task_N3_argument_not_in_interval():

    with pytest.raises(ValueError):
        main.task_N3([1, 2, 3, 4, 5, 6], -250)


def test_task_N3_empty_list():

    with pytest.raises(ValueError):
        main.task_N3([], -2)


def test_task_N3there_is_one_value_in_list():

    with pytest.raises(ValueError):
        main.task_N3([1], 5)

# ******** Задание №1 ***********************************************************************

@pytest.mark.parametrize('n, expected',
                           [(0, 1),
                            (1,1),
                            (7,5040),
                            (20,2432902008176640000)])

def test_factorial_positive(n, expected):

    res = main.factorial(n)

    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_N_argument_is_negative():

    with pytest.raises(ValueError):
        main.factorial(-3)


def test_N_not_range_more_20():

    with pytest.raises(ValueError):
        main.factorial(21)


def test_argument_not_class_int():

    with pytest.raises(TypeError):
        main.factorial(21.5)


def test_factorial_without_arguments():

    with pytest.raises(TypeError):
        main.factorial()

# ******** Задание №2 ***********************************************************************

@pytest.mark.parametrize('n, expected',
                           [(0, [0]),
                            (1, [0,1]),
                            (9, [0,1,1,2,3,5,8,13,21,34])])

def test_fibonacci_positive(n, expected):

    res = main.fibonacci(n)

    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_fibonacci_argument_is_negative():

    with pytest.raises(ValueError):
        main.fibonacci(-7)


def test_fibonacci_without_arguments():

    with pytest.raises(TypeError):
        main.fibonacci()


def test_fibonacci_argument_not_class_int():

    with pytest.raises(TypeError):
        main.fibonacci('')

# ******** Задание №3 ***********************************************************************

@pytest.mark.parametrize('n, expected',
                           [(0, 0),
                            (1, 1),
                            (13, 1101)])

def test_count_ones_positive(n, expected):

    res = main.count_ones(n)

    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_count_ones_argument_is_negative():

    with pytest.raises(ValueError):
        main.count_ones(-7)


def test_count_ones_without_arguments():

    with pytest.raises(TypeError):
        main.count_ones()


def test_count_ones_argument_not_class_int():

    with pytest.raises(TypeError):
        main.count_ones(1.3)

# ******** Задание №3 ***********************************************************************
@pytest.mark.parametrize('n, expected',
                           [(-2 ** 31, False),
                            (2 ** 31-1, False),
                            (123454321, True),
                            (1529251, True),
                            (-1234321, False)])

def test_palindrome_positive(n, expected):

    res = main.palindrome(n)

    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_palindrome_argument_outside_interval_plus():

    with pytest.raises(ValueError):
        main.palindrome(3123542123)


def test_palindrome_argument_outside_interval_minus():

    with pytest.raises(ValueError):
        main.palindrome(-3123542123)


def test_palindrome_without_arguments():

    with pytest.raises(TypeError):
        main.palindrome()


def test_palindrome_argument_not_class_int():

    with pytest.raises(TypeError):
        main.palindrome(1.3)


# ******** Задание №5 ***********************************************************************

def test_positive_transformations_to_date_visiting():

    expected = [[datetime.date.fromisoformat('2023-01-01'),150]]
    res = main.__transformations_to_date_visiting(['2023-01-01,150'])

    assert res == expected, f'Ожидали: {expected} получили:{res}'


def test_transformations_empty_list():

    with pytest.raises(ValueError):
        main.__transformations_to_date_visiting([])


def tets_transformations_not_class_list():

    with pytest.raises(TypeError):
        main.__transformations_to_date_visiting(5)

def test_data_inconsistency_in_list_int():

    with pytest.raises(ValueError):
        main.__transformations_to_date_visiting(['2023-01-01,1.50'])


def test_data_inconsistency_in_list_datetime():

    with pytest.raises(ValueError):
        main.__transformations_to_date_visiting(['2023-01+01,150'])


def test_axis_value_positive():

     array = [[datetime.date.fromisoformat('2023-01-01'),150]]
     expected = [1],[150]

     res = main.__axis_value(array)

     assert res == expected, f'Ожидали: {expected} получили:{res}'


def test__max_visiting_to_month():

    array = [[datetime.date.fromisoformat('2023-01-01'), 150]]
    expected = {1:150}, 150

    res = main.__max_visiting_to_month(array)

    assert res == expected, f'Ожидали: {expected} получили:{res}'


def test__max_visiting_to_day():

    array = [[datetime.date.fromisoformat('2023-01-01'), 150]]
    expected = {6:150}, 150

    res = main.__max_visiting_to_day(array)

    assert res == expected, f'Ожидали: {expected} получили:{res}'


def test_display_visiting_to_month():

    array = [[datetime.date.fromisoformat('2023-01-01'), 150]]
    expected = None

    res = main.display_visiting_to_month(array)

    assert res == expected, f'Ожидали: {expected} получили:{res}'


def test_display_visiting_to_day():

    array = [[datetime.date.fromisoformat('2023-01-01'), 150]]
    expected = None

    res = main.display_visiting_to_day(array)

    assert res == expected, f'Ожидали: {expected} получили:{res}'


def test_data_graph():

    array = ['2023-01-01,150']
    expected = None

    res = main.data_graph(array)

    assert res == expected, f'Ожидали: {expected} получили:{res}'