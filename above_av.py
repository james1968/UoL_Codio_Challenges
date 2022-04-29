def number_of_above_average(A):
  '''implement this function'''
  len_A = len(A)
  len_rows = len(A[0])

  sum = 0
  count = 0
  for i in range(0, len_A):
    for j in range(0, len_rows):
      sum += A[i][j]
      count += 1
  avg = sum / count
  print(avg)

  count1 = 0
  for i in range(0, len_A):
    for j in range(0, len_rows):
      if A[i][j] > avg:
        count1 += 1
      else:
        pass
  print(count1)
  return count1

number_of_above_average([[1,1], [2,4]])