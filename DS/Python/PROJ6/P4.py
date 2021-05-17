def P4(nums):
    # nums: list of int
    count_dit = {}

    for item in nums:
        count_dit.setdefault(item,0)
        count_dit[item] += 1
        
    result = set()

    for keys in list(count_dit.keys()):
        if count_dit[keys] == 1:
            result.add(keys)

    return result