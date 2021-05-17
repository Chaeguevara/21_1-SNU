def P1(num):
    # num: int
    count = 0
    while num >= 1:
        if num % 2 == 1:
            count += 1
        num = num >> 1

    return count


    # return type: int