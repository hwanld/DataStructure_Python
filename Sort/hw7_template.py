def iterative_merge_sort(L):
    sub_len = 1
    while sub_len < len(L):
        index = 0
        while index <= len(L):
            first = index + sub_len
            second = index + sub_len + sub_len
            temp = L[index:second]
            merge(L[index:first], L[first:second], temp)
            L[index:second] = temp
            index += sub_len*2
        sub_len *= 2


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
    L = [1, 9, 3, 2, 6, 7, 3, 4, 14, 2, 36, 44, 21, 94, 0]
    print(L)
    iterative_merge_sort(L)
    print(L)
