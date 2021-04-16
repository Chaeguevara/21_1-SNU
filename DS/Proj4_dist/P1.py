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


root = create_linked_bst([10,5,15,3,7, 9, 18])
print(P1(root, 3, 15 ))

root = create_linked_bst([10,5,15,3,7,None,18])
print(P1(root, 7, 15))

root = create_linked_bst ([10,5,15,3,7,13,18,1,None,6])
print(P1(root,6,10)) 