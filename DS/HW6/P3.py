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
        """
        let's say
        dia = diagonal 
        edge = edge
        dia = 2*edge^2
        and points = p1,p2,p3,p4
        1. cacluate all the distance from p1
            1.1 check if there are only two elements in distance
            ex) distances ={1:[{p1,p2}],2:[{p1,p3}],3:[{p1,p4}]} -> NG. 3 distance
                distances ={1:[{p1,p2},{p1,p3}],3:[{p1,p4}]} ->  2 distance but NG by formula
                distances = {1:[{p1,p2},{p1,p3}],2:[{p1,p4}]} -> O.K by formula
            if passed go next else return False
        2. check the diatance between edge points
            if same as diagonal, pass else false
        
        3.Check diagonal point and edge points distance
            if both same as edge, true

        """    
        
        points_list = [self.p1,self.p2,self.p3,self.p4]
        result = False
        len_point_dict = {}
        
        for i in range(1,4):
            #check duplicated
            if (self.p1.x == points_list[i].x) and (self.p1.y == points_list[i].y):
                return result 
            #calculate all distance
            key = calc_distance_wo_root(p1,points_list[i])
            len_point_dict.setdefault(key, [])
            len_point_dict[key].append(points_list[i])
        #if key_list length != 2, which means several numbers for diagonal or edge, return false
        key_list = len_point_dict.keys()
        if len(key_list) != 2:
            return result
        diagonal = max(key_list)
        edge = min(key_list)

        # check diagonal is power of edge *2
        # also, number of items in diagonal need to be 1 -> check duplication at diagonal position
        if (diagonal != 2*(edge)) or (len(len_point_dict[diagonal]) != 1):
            return result
        
        # gurantee at least one point at diagonal and two points at edge

        #check other diagonal is equalt to the one
        diagonal_pt = len_point_dict[diagonal][0]
        edge_pt1 = len_point_dict[edge][0]
        edge_pt2 = len_point_dict[edge][1]
        if diagonal != calc_distance_wo_root(edge_pt1,edge_pt2):
            return result 
        
        # check other edge distance
        if (edge != calc_distance_wo_root(diagonal_pt,edge_pt1)) or (edge != calc_distance_wo_root(diagonal_pt,edge_pt2)):
            return result 
        
        # now result is true
        result = True

        return result 

def calc_distance_wo_root(p1,p2):
    distance = 0
    distance = (p1.x-p2.x)**2 + (p1.y-p2.y)**2
    return distance


