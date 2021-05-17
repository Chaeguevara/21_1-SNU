def P2(n, edges):
    '''
    n: integer (>=1)
    edges: list of tuples, len(edges) >= 0
    '''
    # <-- ppt #12의 Graph construction과 거의 동일함 -->
    # Vertex리스트 (1~n까지 value)
    V = []
    # edge를 neighbor 딕셔너리
    neighbor = {}
    # 1~n 까지 루프
    for i in range(n):
        #Vectext에 1~n을 더함
        V.append(i+1)
        #1~n 까지 neighbor 빈 리스트 생성
        neighbor[i+1] = []
    #Edge 루프
    for (v,w) in edges:
        #서로 pair를 만듬
        neighbor[v].append(w)
        neighbor[w].append(v)
    # <-- ppt #12의 Graph construction과 거의 동일함 -->

    #visited dictionary생성
    visited = {}

    #p2 Helper
    def p2Helper(neighbor,v,visited):
        #들어온 vertex -> False로 visited dictionary 설정
        visited[v] = False
        # 해당 vertex의 neighbor가 존재한다면
        if len(neighbor[v]) != 0:
            #각 Neighbor에 대해
            for item in neighbor[v]:
                # neighbor가 방문한 적이 없다면 
                if visited.get(item,-1) == -1:
                    # recursion
                    p2Helper(neighbor,item,visited)
        
        # visited의 length return
        return len(visited)
    # count = helper의 value. helper에 1 넣음
    count = p2Helper(neighbor,1,visited)
    print(count)


    return count

P2(4, [(1, 2), (2, 1)])