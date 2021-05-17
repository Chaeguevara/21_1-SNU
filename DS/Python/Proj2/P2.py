"""
**Instruction**
Please see instruction document.

"""


def P2(parentheses: str) -> bool:
    print('hi')
    #base case. odd length
    if len(parentheses) % 2 == 1:
        return False
    
    # check all are (){}[]
    paren_set = "(){}[]"
    paren_front = "({["
    paren_end = ")}]"
    for item in parentheses:
        if item not in paren_set:
            return False

    # base case. need to start from paren_front "({["
    if parentheses[0] not in paren_front:
        return False
    

    # check biggest pair [.......]
    for i in range(len(paren_front)):
        # Check which is opening parenthesis "{[("
        if parentheses[0] == paren_front[i]:
            ending_paren = paren_end[i]
            # find closing parenthesis index from the end
            for j in range(len(parentheses)-1, 0, -1):
                print(j)
                #if foudn assign to variable
                if parentheses[j] == ending_paren:
                    end_index = j
                    break
                # if not found, false'[{}' something like this shape
                if j == 0:
                    return False
            break
    # [......] case
    if (end_index+1) == len(parentheses):
        #if length == 2, return true
        if len(parentheses) == 2:
            return True
        # else recursive
        else:
            return P2(parentheses[1:-1])
    #[....]{....} like this
    else:
        # recursive for former and latter
        if j == 1:
            result1 = True
        else:
            result1 = P2(parentheses[1:j])
        result2 = P2(parentheses[j+1:])
        print(parentheses[j+1:])
        if result1 and result2:
            return True
        else:
            return False
    ##### End of your code #####


