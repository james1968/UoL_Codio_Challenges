def trim_matrix(M):
  '''implement this function'''
  len_rows = len(M)
  n = len(min(M, key=len))
  for i in range(0, len_rows):
    M[i] = M[i][:n]
  print(M)
X = [[1,2,3],[12,13],[21,22,23,24]]
trim_matrix(X)