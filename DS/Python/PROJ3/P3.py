def P3(A, B):
    '''
    A, B: list
    '''
    '''
    loop with same index
    get sum with the index
    if sum equals each other -> add count
    else -> initilize count,sum and add count to list or something
    get the max and return
    '''
    sum_a = sum(A)
    sum_b = sum(B)
    length = len(A)
    start = 0
    end = length - 1
    def p3helper(sum_a,sum_b,A,B,length,start,end):
        if length == 1:
            return -1
        if start >= end:
            return -1
        if sum_a == sum_b:
            return length
        if sum_a < sum_b:
            if (A[start] == 0) and (B[start] == 1):
                sum_b -= 1
                start += 1
            elif(A[end] == 0) and (B[end] == 1):
                sum_b -= 1
                end -= 1
            elif(A[start] == 0) and (B[start] == 0):
                start += 1
            elif(A[end] == 0) and (B[end] == 0):
                end -= 1
            elif (A[start] == 1) and (B[start] == 1):
                start += 1
                sum_b -= 1
                sum_a -= 1
            elif (A[end] == 1) and (B[end] == 1):
                end -= 1
                sum_b -= 1
                sum_a -= 1
            length -= 1
            return p3helper(sum_a,sum_b,A,B,length, start, end)
        else:
            return p3helper(sum_b,sum_a,B,A,length, start, end)    
        
    return p3helper(sum_a,sum_b,A,B,length,start,end)


        


  