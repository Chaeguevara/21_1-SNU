"""
**Instruction**
<Factor into two prime numbers>
Input of P2 function is natural number.
P2 function returns whether the input nubmer could be factored into two prime numbers.
Do not worry about invalid input.

>>> P2(6) #2 * 3
True

>>> P2(9) #3 * 3
True

>>> P2(12) # 2 * 2 * 3
False

>>> P2(7) # 7
False


"""

def P2(n:int) -> bool:        
    ##### Write your Code Here #####
    """
    Key stratedgy: if input number is n
    - go through 1 to n-1
    - if n % i == 0, get n % i and n//i. n % i will be primary number
    - check if n // i primary number. if then, return the number
    """
    #Helper function
    def isAPrimary(n):
        if n ==1:
            return False
        result = False
        counter = 0
        for i in range(2,n+1):
            counter += 1
            if (n % i == 0):
                break 
        if counter == n-1:
            result = True
        return result
    #initialize parameter
    result = False
    counter = 0
    multiplier = 1
    other_multi = 1
    is_othermulti_primary = False
    # base case. if 2 return false
    if n == 2 or n == 1:
        return False
    # get multiplier and othermultiplier
    for i in range(2,n):
        counter += 1
        remainder = n % i
        if remainder == 0:
            multiplier = i
            other_multi = n//i
            is_othermulti_primary = isAPrimary(other_multi)
            break
    
    #Check cases
    #1. gone through all the loop(check by counter). -> No primary in between 2 to n-1
    if counter == (n-2):
        return False
    #check other multiplier primary
    if is_othermulti_primary:
        result = True
    print(multiplier,other_multi)
    #return result
    
    return result
    ##### End of your code #####
