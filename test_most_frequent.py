from topic6_most_freq import most_frequent
import pytest


def test_one():
    # most straightforward test
    L = [2, 1, 2]
    assert most_frequent(L) == 2


def test_two():
    # long list
    L = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 3]
    assert most_frequent(L) == 3


def test_three():
    # several most frequent
    L = [30, 20, 20, 30, 40, 30, 20]
    assert most_frequent(L) == 20


def test_four():
    # with negative integers
    L = [-5, 10, 20, -10, -10]
    assert most_frequent(L) == -10


def test_five():
    # smallest possible list
    L = [5]
    assert most_frequent(L) == 5