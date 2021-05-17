def singleNum(nums): 
    ans=0
    for i in range(1, len(nums)) :
        ans ^=nums[i] 
        print (ans)


    return ans 