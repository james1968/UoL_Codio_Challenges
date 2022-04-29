def number_of_differences(A, B):
  '''implement this function'''
  len_rows_A = len(A)
  print(len_rows_A)
  len_rows_B = len(B[0])
  print(len_rows_B)

  count = 0
  for i in range(0, len_rows_A):
    print("i:", i)
    for j in range(0, len_rows_B):
      print("j:", j)
      print("A:", A[i][j])
      print("B:", B[i][j])
      if A[i][j] != B[i][j]:
        count += 1
        print("count:", count)
      else:
        pass
  print(count)

number_of_differences([[1,2,3], [4,5,6]], [[1,2,4], [3,5,6]])