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
            curNode.left = None
        if curNode.val > high:
            curNode.right = None
        if (curNode.val >= low) and (curNode.val <= high):
            sumVal += curNode.val

        # recursive case
        if (curNode.left):
            sumVal = sumHelper(curNode.left, low, high, sumVal)
        if (curNode.right):
            sumVal = sumHelper(curNode.right, low, high, sumVal)

        return sumVal

    
    sumVal = sumHelper(root, low, high, sumVal)

    return sumVal
    ##### End of your code #####

