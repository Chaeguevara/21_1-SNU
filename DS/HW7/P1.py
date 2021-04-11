def P1(lst):
    """bubble sort
    go through all elements
    i in range(len(list)-1)
    -> compare list[i], list[i+1]
    stop loop when there is no more swap
    """
    count = 0
    swap = True
    while swap == True:
        swap = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                count += 1
                swap = True
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    return count
