from typing import *

A: List[int] = [x * 2 for x in [0, 1, 2]]


B: Set[int] = {x * 2 for x in [0, 1, 2]}


C: Dict[int, int] = {x: x / 2 for x in [0, 1, 2]}  # dictionary


D: Iterator[int] = iter([1, 2, 3])


E: Any = (x ** 2 for x in {1.0, 2.1, 3.3})


F: Any = set(D)


G: Any = zip([1, 2, 3], ('a', 'b', 'c'))


def f(x: int) -> float:
    return x / 2


H: Any = [f(x) for x in [1, 2, 3]]


I: Any = map(f, [1, 2, 3])
print("I")
print(I)

J: Any = map(f, D)
print("J")
print(J)

K: Any = enumerate(I, start=1)

print("K")
print(K)
print(list(K))