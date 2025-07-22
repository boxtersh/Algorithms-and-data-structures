import pytest
from main import output_minimum_number_greatest_repetition as function

@pytest.mark.parametrize('lst, expected',
                           [([], -1),
                            ([1,1,2,2,3,3,4,4,4], 4),
                            ([-1,-1,2,2,3,3,4,4], -1),
                            ([1,1,1,1,1,1,1,1], 1),
                            ([-1,-1,-1,-1,-1,-1,-1,-1], -1),
                            ([1,2,3,4,5,6,7,8], 1),
                            ([9,4,7,1,5,3,5,9,2,8], 5)])

def test_output_minimum_number_greatest_repetition(lst, expected):

    res = function(lst)

    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_type_date_not_list():

    with pytest.raises(TypeError):
        function('')