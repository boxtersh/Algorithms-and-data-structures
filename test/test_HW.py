import pytest
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
