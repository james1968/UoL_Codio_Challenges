s = input()
s_lis = list(map(int, s.split()))

ans = []
for i in range(0, len(s_lis), 2):
  sub_s = s_lis[i:i+2]
  sub_s.reverse()
  ans.append(sub_s)

st_ans = ''
for i in ans:
  for j in i:
    st_ans += str(j)

print(st_ans)