from delete_every_2nd import delete_every_2nd
import pytest

def test_1():
  assert delete_every_2nd("aabcdaaaxyaa11aa2", "aa") == "aabcdaxyaa112"

def test_2():
  assert delete_every_2nd("aabbaabbaa", "aa") == "aabbbbaa"

def test_3():
  assert delete_every_2nd("aabbbaabbbaabbb", "aa") == "aabbbbbbaabbb"

def test_4():
  assert delete_every_2nd("bcdaaaxy11245aatreaappp", "aa") == "bcdaaaxy11245treaappp"

def test_5():
  with pytest.raises(ValueError):
    delete_every_2nd("aabcdaaaxyaa11aa2", "")

def test_6():
  with pytest.raises(ValueError):
    delete_every_2nd("", "aa")