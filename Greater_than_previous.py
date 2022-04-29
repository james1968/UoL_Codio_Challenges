seq = []

n = input()
print(n)

while True:
  seq.append(n)

print(n)
ans = []
for i in range(0, len(seq)):
  if seq[i+1] > seq[i]:
    ans.append(seq[i + 1])

print(ans)