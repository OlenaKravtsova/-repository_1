
from Hellel.October_2023_Home.Home_work_7.home_work_7 import sorting_list_of_numbers, sorting_list_descending, sorting_list_of_words

# Тест для sorting_list_of_numbers
def test_sorting_list_of_numbers():
    input_numbers: [int] = [8, 1, 4, 2, 5, 9, 3, 6, 7]
    result: [int] = sorting_list_of_numbers(*input_numbers)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Тест для sorting_list_descending
def test_sorting_list_descending():
    input_numbers: [int] = [8, 1, 4, 2, 5, 9, 3, 6, 7]
    result: [int] = sorting_list_descending(*input_numbers)
    assert result == [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Тест для sorting_list_of_words
def test_sorting_list_of_words():
    input_words: [str] = ["apple", "pineapple", "kiwi", "orange", "plum"]
    result: [str] = sorting_list_of_words(*input_words)
    assert result == ['kiwi', 'plum', 'apple', 'orange', 'pineapple']
