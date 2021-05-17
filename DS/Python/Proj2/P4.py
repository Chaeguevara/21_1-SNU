"""
**Instruction**
Please see instruction document.

"""
from linked_list_helper import ListNode
def P4(head: ListNode) -> ListNode: 
    ##### Write your Code Here #####
    # base case. when node is empty or length == 1
    if head is None:
        return None
    if head.next is None:
        return head
    # create start node
    start_node = ListNode()
    cur_start_node = start_node
    cur_head_node = head
    # add from the last 
    while cur_head_node != None:
        new_first = ListNode(cur_head_node.val)
        new_first.next = cur_start_node.next
        cur_start_node.next = new_first
        cur_head_node = cur_head_node.next
             
    
    return cur_start_node.next
    ##### End of your code #####

