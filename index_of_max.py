seq = []

while True:
  n = int(input())
  if n == 0:
    break
  else:
    seq.append(n)

print(seq.index(max(seq)))



