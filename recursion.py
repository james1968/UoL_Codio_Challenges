calls = 0
def fib(n, count= 0):
    global calls
    calls += 1
    print(calls)

    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

fib(3)
print("---")
fib(4)
print("---")
fib(5)
print("---")
fib(6)
print("---")
fib(7)