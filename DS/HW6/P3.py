class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    
    def is_square(self):
        
        # return: boolean