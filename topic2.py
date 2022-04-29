def fun(n):
  sum = 0
  for i in range(0,n):
    sum+=i
  return sum

print(fun(5))

def fun1( n ):
  m = 0
  sum = 0

  while m < n:
    m+=1
    sum+=m
  return sum

print(fun1(5))

def fun2( n ):
  m = 0
  sum = 0

  while m < n:
    sum+=m
    m+=1
  return sum

print(fun2(5))

def fun3( n ):
  sum = 0

  for i in range(n,1,-1):
    sum+=i
  return sum

print(fun3(5))