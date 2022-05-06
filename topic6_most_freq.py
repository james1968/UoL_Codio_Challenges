def most_frequent(L):
  '''implement this function'''
  ans = dict()
  for i in range(0, len(L)):
    count = 0
    for j in range(0, len(L)):
      if L[i] == L[j]:
        count += 1
        ans[L[i]] = count
  max_number = ans[max(ans, key=ans.get)]
  print(max_number)
  ans_arr = []
  for key, value in ans.items():
    if max_number == value:
      ans_arr.append(key)
  print(min(ans_arr))
  return min(ans_arr)

most_frequent([30, 20, 20, 30, 40, 30, 20])


