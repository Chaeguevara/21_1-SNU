import linked_list_helper as llist

left = llist.create_linked_list([1,2,3,4,5])
new_list = llist.create_linked_list([7,8,10])
head = left
llist.print_linked_list(head, [])
left = left.next
llist.print_linked_list(left, [])
curr = head
llist.print_linked_list(curr, [])
curr.next = new_list
llist.print_linked_list(curr, [])
llist.print_linked_list(head, [])
