
# test eset - python függvény
from functions_3rd_day import get_max


def test_get_max():

    #given
    a = 5
    b = 10
    #when: megkapjuk az aktuális értéket
    result = get_max(a, b)
    #then - aktuális érték = elvárt érték?
    assert result == 10


def test_get_max_when_first_value_is_greater():
    assert get_max(200 ,5) == 200


def test_get_max_equal_values():
    assert get_max(100, 100)  == 100


