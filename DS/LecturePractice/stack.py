class LinkedNode():
    def __init__(self,x):
        self.val = x
        self.next = None

class myStack():
    def __init__(self,x):
        self.sentinel = LinkedNode(0)
        self.size = 0


    def push(self,x):
        self.size += 1
        curNode = self.sentinel
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = LinkedNode(x)


    def getSize(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False



