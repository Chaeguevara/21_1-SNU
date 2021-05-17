"""
**Instruction**
Please see instruction document.

"""
from linked_list_helper import ListNode
def P3(head: ListNode) -> ListNode: 
    # base case. when node is empty or length == 1
    if head is None:
        return None
    if head.next is None:
        return head
    
    # Find the number of nodes
    cnt = 0
    curr = head
    midNode = head
    #iterate all over the node
    while curr != None:
        curr = curr.next        
        cnt += 1

    #Divide into left and right
    mid = cnt // 2    
    left= head
    curr = head
    cnt = 0
    while cnt < mid-1:
        curr = curr.next
        cnt += 1
    right = curr.next
    #by putting None, cut node
    curr.next = None 

    # result of P3 by left becomes P3
    # result of P3 by right becomes P3
    left = P3(left)
    right = P3(right)

    #define merge function
    def merge(left,right):
        
        curr_left = left
        curr_right = right
        #start node(dummy). Used for connecting nodes
        start_node = ListNode()
        # while left node or right node is not None        
        while (curr_left != None) and (curr_right != None):
            #copy of cur node
            cur_node = start_node
            # if value of left is smaller than right
            if curr_left.val <= curr_right.val:
                # add the left value to start node
                while cur_node.next != None:
                    cur_node = cur_node.next
                # to go next step, set node to next
                cur_node.next = ListNode(curr_left.val)
                curr_left = curr_left.next
            #else, do similar
            else:
                while cur_node.next != None:
                    cur_node = cur_node.next
                # to go next step
                cur_node.next = ListNode(curr_right.val)
                curr_right = curr_right.next
        
        # add remaining to last  
        cur_node = start_node
        while cur_node.next != None:
            cur_node = cur_node.next
        # if left has remaining value
        if curr_left != None:
            # add to entire node
           cur_node.next=curr_left
        else:
            #else do similar
            cur_node.next=curr_right
        # return next of start_node as we started from dummy
        start_node = start_node.next 
        return start_node
    
    return merge(left,right) 

