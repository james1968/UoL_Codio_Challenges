n = int(input())
fib_seq = [0, 1]
fib_seq_num = 0
i = 2
while fib_seq_num < n:
  fib_seq_num = (fib_seq[i - 1] + fib_seq[i - 2])
  fib_seq.append(fib_seq_num)
  i += 1

if n in fib_seq:
  print(fib_seq.index(n))
else:
  print(-1)

