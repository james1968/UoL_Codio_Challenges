def swap_columns(M, i, j):
  '''provide your implementation'''
  len_rows = len(M)
  len_col = len(M[0])
  temp = 0
  for k in range(0, len_rows):
    for l in range(0, len_col):
      if l == i:
        temp = M[k][i]
        print(temp)
        temp2 = M[k][j]
        M[k][i] = temp2
        M[k][j] = temp
  print(M)

M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
swap_columns(M, 0, 1)