from time import time


def prefix_average1(S):
    n = len(S)
    A = [0]*n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total / (j+1)
    return A

# Looks Better


def prefix_average2(S):
    n = len(S)
    A = [0]*n
    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)
    return A

# Linear Time


def prefix_average3(S):
    n = len(S)
    A = [0]*n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total/(j+1)
    return A


S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(prefix_average1(S))
# print(prefix_average2(S))
# print(prefix_average3(S))
