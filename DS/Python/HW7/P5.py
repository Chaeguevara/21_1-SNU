def P5(lst):
    result = 0
    expected1 = len(lst)
    expected2 = 1
    count = len(lst)
    for i in range(len(lst)-1,-1,-1):
        if lst[i] == expected1:
            expected1 -= 1
    for i in range(len(lst)):
        if lst[i] == expected2:
            expected2 += 1
            count -= 1

    if expected1 < count:
        result = expected1
    else:
        result = count
    print(expected1,count)
    return result