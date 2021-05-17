class LinkedNode():
    def __init__(self,x:int)-> None:
        self.val = x
        self.next = None


    """
    Mystack
    Four methods
    push(x) : add a LinkedNode that val = x to myStack
    pop: Remove the most recently added LinkedNode from Mystack
    top: Return val of the most recently added LinkedNode
    getSize: number of linked nodes in myStack
    isEmpty: Return True if empyt, otherwise False
    """

class myStack():
    def __init__(self) -> None:
        self.sentinel = LinkedNode(0)
        self.size = 0

    def push(self,x:int) -> None:
        newNode = LinkedNode(x)
        newNode.next = self.sentinel.next
        self.sentinel.next = newNode
        self.size += 1
    
    def pop(self) -> None:
        if not self.isEmpty():
            removal = self.sentinel.next
            self.sentinel.next = self.sentinel.next.next
            removal.next = None
            self.size -= 1
    
    def top(self) -> int:
        if not self.isEmpty():
            return self.sentinel.next.val
        else:
            return None

    def getSize(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

a = myStack()
print (a.isEmpty())

a.push(10)
print (a.isEmpty(),a.getSize(),a.top())
a.push(20)
print (a.isEmpty(),a.getSize(),a.top())
a.push(30)
print (a.isEmpty(),a.getSize(),a.top())
a.pop()
print (a.isEmpty(),a.getSize(),a.top())
a.pop()
print (a.isEmpty(),a.getSize(),a.top())
a.pop()
print (a.isEmpty(),a.getSize(),a.top())
a.pop()
print (a.isEmpty(),a.getSize(),a.top())
