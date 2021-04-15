class undi_graph():
    def __init__(self,V: list, E: list) -> None:
        self.V = V[:]
        self.neighbor = {}
        # neighbor is best for representing edge
        for v in V:
            self.neighbor[v] = []
        for (v,w) in E:
            self.neighbor[v].append(w)
            self.neighbor[w].append(v)

V = [0,1,2,3,4,5,6,7,8,9]
E = [(0,1),(1,4),(1,5),(4,6),(5,6),(0,1),(0,1),(0,1),]