class LinkedNode():
    def __init__(self, x):
        self.val = x
        self.next = None

a = LinkedNode(5)
b = LinkedNode(7)

a.next = b
curNode = a
while curNode:
    print(curNode.val)
    curNode = curNode.next

L = SLList()
L.addfirst(5)
L.addfirst(10)
L.getFist()
    