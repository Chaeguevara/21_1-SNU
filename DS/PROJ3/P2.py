def P2(nums):
    '''
    nums: list
    '''
    prev = -1
    result_list = []
    count = 0
    for i in range(len(nums)):
        if i == 0:
            prev = nums[i]
            continue
        if prev != nums[i]:
            count += 1
            print(i,count)
            if i == (len(nums)-1):
                result_list.append(count)
        else:
            result_list.append(count)
            count = 0
        prev = nums[i]
        # print(prev)

    result_set = set(result_list)
    max_val = max(result_set)
    print(result_list)
    return max_val

