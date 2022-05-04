def twoxtwomatrix(n):
  '''creates a 2x2 matrix with n in each position'''
  X = [n, n]
  Y = [X, X]
  print(Y)
  return Y

M = twoxtwomatrix(7)

def vectorise(n, m):
  '''creates a tuple of element n repeated m times'''
  T = () #empty tuple
  counter = 0
  while counter < m:
    T = T + (n,) #in Python (n,) is a tuple with one element n
    counter+=1
  #as a result T, is tuple of arbitrary length
  print(T)
  return T

Corners = {(-1, -1), (1,-1), (-1,1)}
is_top_right_present = (1,1) in Corners
print(is_top_right_present)

L = vectorise(100, 5)