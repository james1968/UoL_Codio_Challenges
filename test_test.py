from frequency_in_text_file import frequency_in_text
import pytest

def test_1():
  assert frequency_in_text("Apple.", "Apple") == pytest.approx(1, 0.0001)

def test_2():
  assert frequency_in_text("One apple. One more apple and another apple.", "apple") == pytest.approx(3/2, 0.0001)

def test_3():
  assert frequency_in_text("This baobab is the biggest of all baobabs. baobabaobab. And another baobab.", "baobab") == pytest.approx(4/3, 0.0001)

def test_4():
  assert frequency_in_text("xyz aaa xyz. xyz aaa xyz. xyz aaa xyz. xyz aaa xyz.", "xyz") == pytest.approx(2, 0.0001)

def test_5():
  assert frequency_in_text("abc def.", "xyz") == pytest.approx(0, 0.0001)

def test_6():
  with pytest.raises(ValueError):
    frequency_in_text("abc def", "a")  