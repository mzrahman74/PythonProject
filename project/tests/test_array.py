import pytest
from project.src.array import find_second_highest, third_highest, has_duplicate


def test_find_second_highest():
    assert find_second_highest([10, 5, 10, 6, 4, 11 ]) == 10

def test_find_second_highest_empty():
    assert find_second_highest([]) is None

def test_find_second_highest_negative():
    assert find_second_highest([-10, -5, -10,-6,-4, -11]) == -5

def test_find_third_highest():
    assert third_highest([10, 20, 55, 65, 70]) == 55

def test_find_third_highest_empty():
    assert third_highest([]) is None

def test_find_third_highest_negative():
    assert third_highest([-10, -5, -10,-6, -11]) == -10

def test_find_duplicate_numbers():
    assert has_duplicate([10, 10, 12, 15, 80, 100]) == True