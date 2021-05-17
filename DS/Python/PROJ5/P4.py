import math
def P4(L, T):
    '''
    L: current location of Luffy, 0<=L<=100000, integer
    T: location of treasure, 0<=T<=100000, integer
    '''
    value_set = set()
    neighbor = {}
    if L == T:
        return 0
    # def p4Helper(value_set, L, T, neighbor):
    #     # Out of range
    #     if L < 0:
    #         return
    #     # Out of range
    #     if L > 100000:
    #         return
    #     # 도달한 경우
    #     if L == T:
    #         return
    #     # 이미 방문한 경우
    #     if L in value_set:
    #         return
    #     # value의 neighbor 생성
    #     neighbor.setdefault(L, [])
    #     # value set에 넣음. -> 나중에 방문했는지 체크하기 위해
    #     value_set.add(L)
    #     if (L-1 >= 0):
    #         neighbor[L].append(L-1)
    #         print(L,value_set)
    #         p4Helper(value_set, L-1, T, neighbor)
    #     if (L+1 <= T):
    #         neighbor[L].append(L+1)
    #         print(L,value_set)
    #         p4Helper(value_set, L+1, T, neighbor)
    #     if (2*L <= 2*T):
    #         neighbor[L].append(2*L)
    #         print(L,value_set)
    #         p4Helper(value_set, 2*L, T, neighbor)

    def p4Helper(value_set, L, T, neighbor):
        new_list = [L]
        depth = 0
        while len(new_list) != 0:
            print(new_list)
            item = new_list.pop()
            if item < 0:
                break
            if item > 100000:
                break
            if item == T:
                break
            if item in value_set:
                continue
            value_set.add(item)
            neighbor.setdefault(item, [])
            if (item-1) >= 0 and (item-1) not in value_set:
                neighbor[item].append(item - 1)
                new_list.insert(0,item -1)
            if (item+1) <= T and (item+1) not in value_set:
                neighbor[item].append(item + 1)
                # if(item + 1) in value_set:
                #     continue
                new_list.insert(0,item + 1)
            if not item > T and (2*item) not in value_set:
                if item*2 == item + 1:
                    continue
                neighbor[item].append(item *2)
                # if(2*item) in value_set:
                #     continue
                new_list.insert(0,item * 2)
            depth += 1
        if L > T:
            return depth

        return int(math.log2(depth))


P4(5, 17)
# return type: integer
