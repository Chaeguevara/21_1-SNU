"""
**Instruction**
Please see instruction document.
"""
from BST_Helper import *


def P3(root: TreeNode, val: int) -> TreeNode:
    ##### Write your Code Here #####
    # Get the height of each node
    count_val = 0

    # 현재 노드의 모든 Children(leaf까지)의 갯수를 return한다
    def getCount(curNode: TreeNode, count_val) -> int:
        if not curNode:
            return count_val
        count_val += 1
        if curNode.left:
            count_val = getCount(curNode.left, count_val)
        if curNode.right:
            count_val = getCount(curNode.right, count_val)
        return count_val

    # 현재 노드를 기준으로 왼쪽과 오른쪽의 노드 갯수의 차이를 구한후 return 한다
    def getBalance(curNode: TreeNode) -> int:
        result = 0
        count_left = 0
        count_right = 0
        count_left = getCount(curNode.left, count_left)
        count_right = getCount(curNode.right, count_right)
        result = count_left - count_right
        return result

    def rightRotation(curNode):
        middle = TreeNode(curNode.left.val)
        

    def leftRotation(curNode):
        sentinel = TreeNode(0)
        sentinel.left = curNode.right
        sentinel.left.left = curNode
        if curNode.right.left:
            sentinel.left.left.right = curNode.right.left
        sentinel.left.right = curNode.right.right
        return sentinel.left
    count_val = getCount(root.right,count_val)

    new_root = rightRotation(root)
    print(new_root.printTree())
    # print(new_root.val, new_root.left.val, new_root.left.right.val)
    # new_root = leftRotation(new_root)
    return new_root
    ##### End of your code #####

root = create_linked_bst( [7,3,8,2,5,None,9])
fullbst = P3(root,0)
print(fullbst.printTree())

