"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *
def P2(root: TreeNode):       

    result = []
    depth = 0
    depth_dict = {}
    
    def P2Helper(depth,depth_dict,curNode):
        #base case
        if not curNode:
            return depth_dict
        else:
            depth_dict.setdefault(depth,[])
            depth_dict[depth].append(curNode.val)

        if curNode.left or curNode.right:
            depth += 1
        
        if curNode.left:
            depth_dict = P2Helper(depth,depth_dict,curNode.left)
        if curNode.right:
            depth_dict = P2Helper(depth,depth_dict,curNode.right)

        return depth_dict
    depth_dict = P2Helper(depth,depth_dict,root)
    key_list = sorted(list(depth_dict.keys()))
    key_list.reverse()

    for key in key_list:
        result.append(depth_dict[key])

    return result
    ##### End of your code #####

