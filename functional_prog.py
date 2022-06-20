from typing import Callable, Any  #do not change this line
def my_abs(x: float) -> float:
    if x >= 0:
        return x
    else:
        return -x


def double(f: Callable[[float], float]) -> Callable[[float], float]:
    def new_func(x: Callable[[float], float]) -> float:
        result = 2 * f(x)
        return result

    return new_func


double_abs = double(my_abs)