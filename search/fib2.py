def fib(n):
    if n <= 1:
        return 1
    
    return fib(n-1) + fib(n-2)

for n in range(40):
    print(fib(n), end = " ")