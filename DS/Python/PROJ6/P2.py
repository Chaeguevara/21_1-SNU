def P2(x, y):
    num = x^y
    count = 0
    while num >= 1:
        if num % 2 == 1:
            count += 1
        num = num >> 1

    return count
