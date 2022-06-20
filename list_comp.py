from typing import Iterator
from typing import Callable
import math

X = [3, 4, 5, 6, 7]
Y = (1, 2, 3, 4, 5)

ans = {(x, y) for x in X for y in Y if x < y}


X_1 = [1,2,3]
Y_1 = [5,6,7]
S = zip(X_1, [(y**2) for y in Y_1])

X_e = [1,10,3,4,10,5]
ans_e = [(idx) for idx, num in (enumerate(X_e)) if num == max(X_e)]


def f(x: str) -> str:
  s = ''
  for l in x:
    if l in {'a', 'e', 'i', 'o', 'u'}:
      s += chr(ord(l)-32)
    else:
      s += l
  return s


def stringify(f: Callable[[str], str])-> Callable[[str], str]:
    def f(x: str) -> str:
        s = ''
        for l in x:
            s += chr(ord(l) - 32)
        print(s)
        return s
    return f


str_to_upper = stringify(f)
str_to_upper("apple")

def square(x: float)-> float:
  return x*x

def indices_of_high(f: Callable[[float], float], bound: float, L: list[float])-> set[float]:
     '''implement this function by a single line of the form
     return YOUR_EXPRESSION
     where YOUR_EXPRESSION is a single comprehension expression
     '''
     square

print(indices_of_high(square, 7.5, [0.5, 20.0, 2.0, 3.1]))

print(indices_of_high(math.sqrt, 1.0, [0.5, 20.0, 2.0, 3.1]))

