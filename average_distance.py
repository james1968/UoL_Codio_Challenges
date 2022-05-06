import math
def average_distance(coordinates):
  '''implement this function'''
  if len(coordinates) < 2:
    raise ValueError
  ans = []
  for i in range(0, len(coordinates)-1):
    ans.append(math.sqrt(((coordinates[i][0] - coordinates[i+1][0]) ** 2) + ((coordinates[i][1] - coordinates[i+1][1]) ** 2)))
    if i+2 < len(coordinates):
      ans.append(math.sqrt(((coordinates[i][0] - coordinates[i+2][0]) ** 2) + ((coordinates[i][1] - coordinates[i+2][1]) ** 2)))
  number = len(coordinates)
  final_ans = sum(ans) / number
  print(final_ans)
  return float(final_ans)

average_distance([(3,5), (4, 6), (6, 8)])
