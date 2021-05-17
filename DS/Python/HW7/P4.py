def P4(A, B):
    result = 0
    A_sorted = sorted(A)
    B_sorted = sorted(B)
    for i in range(len(A_sorted)):
        result += A_sorted[i]*B_sorted[len(A_sorted)-1-i]

    return result

