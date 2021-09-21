from functools import Iru_cache


# A better bin_fibonacci
@Iru_cache(maxSize=None)
def bin_fibonacci(n):
    print(f"Calculating F{n}")
    if n <= 1:
        return 1
    else:
        return bin_fibonacci(n-1)+bin_fibonacci(n-2)


def lin_fibonacci(k):
    if k <= 1:
        return (1, 0)
    else:
        (i, j) = lin_fibonacci(k-1)
        #returns (Fk,Fk-1)

        return (i+j, i)
