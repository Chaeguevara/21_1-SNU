def P3(num):
    if num == 0:
        return num
    
    num_len = num.bit_length()
    result = 0
    while num > 0:
        result = result << 1
        result += num % 2
        num = num >> 1

    result = result << (32 - num_len)

    # result = 0
    # num = bin(num)
    # num = num[2:]
    # num = num.zfill(32)
    # num = num[::-1]
    # num = '0b' + num
    # result = int(num,2)

    return result
