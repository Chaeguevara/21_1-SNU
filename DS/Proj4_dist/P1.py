"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *


def P1(root: TreeNode, low: int, high: int) -> int:
    ##### Write your Code Here #####
    sumVal = 0

    def sumHelper(curNode, low, high, sumVal):
        # base case
        if not curNode:
            return sumVal
        if curNode.val < low:
            return sumVal
        if curNode.val > high:
            curNode.right = None
        print(curNode.printTree())
        # recursive case
        if (curNode.left) and (curNode.left.val >= low):
            sumVal = sumHelper(curNode.left, low, high, sumVal + curNode.left.val)
        if (curNode.right) and (curNode.right.val <= high):
            sumVal = sumHelper(curNode.right, low, high, sumVal + curNode.right.val)

        print(sumVal)
        return sumVal

    
    sumVal = sumHelper(root, low, high, sumVal)

    return sumVal
    ##### End of your code #####


root = create_linked_bst([10,5,15,3,7, 9, 18])
print(P1(root, 3, 9 ))
