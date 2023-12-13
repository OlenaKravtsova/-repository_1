import pytest
from home_work_10 import add_three_numbers_and_log

# solution 1
def test_1():
    assert add_three_numbers_and_log(3, 4,7) == 14

def test_2():
    assert add_three_numbers_and_log(13, 4, 20) == 37

def test_3():
    assert add_three_numbers_and_log(1, 4, 5) == 10

# solution 2
@pytest.mark.parametrize("numb_1, numb_2, numb_3, result",[
    pytest.param(3, 4, 7, 14, id="standard"),
    pytest.param(3, -3, 4, 4, id="negative and positive"),
    pytest.param(10, -1, -4, 5, id="two negative")])
def test_set_1(numb_1, numb_2, numb_3, result):
    assert add_three_numbers_and_log(numb_1, numb_2, numb_3) == result

# solution 3
list_test = [(3, 4, 7, 14), (3, -3, 4, 4), (10, -1, -4, 5)]
@pytest.mark.parametrize("numb_1, numb_2, numb_3, result", list_test)
def test_set_2(numb_1, numb_2, numb_3, result):
    assert add_three_numbers_and_log(numb_1, numb_2, numb_3) == result

