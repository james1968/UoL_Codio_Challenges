from average_distance import average_distance
import pytest

def test_1():
  assert abs(average_distance([(1,2), (3,4), (5,6)]) - 3.771) < 0.001

  assert abs(average_distance([(2,5), (4,6), (6,8)]) - 3.354) < 0.001

  assert abs(average_distance([(2, 5), (4, 6), (6, 8), (7, 9)]) - 3.9303) < 0.001

  assert abs(average_distance([(2, 4), (4, 6), (6, 8), (7, 10)]) - 4.6374) < 0.001

def test_2():
  with pytest.raises(ValueError):
    average_distance([(1,2)])