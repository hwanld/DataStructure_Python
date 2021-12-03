def merge_sort(L):
    n = len(L)
    if n < 2:
        return

    mid = n // 2
    L1 = L[:mid]
    L2 = L[mid:]

    merge_sort(L1)
    merge_sort(L2)

    merge(L1, L2, L)


def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1


if __name__ == "__main__":
    L = [1, 9, 8, 2, 6, 3, 4, 5, 10]
    print(L)
    merge_sort(L)
    print(L)
