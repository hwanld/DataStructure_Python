def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n*recursive_factorial(n-1)


def iterative_factorial(n):
    fact = 1
    for val in range(1, n+1):  # 1부터 n까지
        fact *= val
    return fact


print(recursive_factorial(5))
print(iterative_factorial(5))
