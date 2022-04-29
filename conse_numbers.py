def cons_number():
  count = 1
  count_max = 0
  n = int(input())
  while True:
    if n == 0:
      break
    m = int(input())
    if m == n:
      count += 1
      print(count)
    else:
      if count > count_max:
        count_max = count
        count = 1

    n = m
  print(count_max)

cons_number()


