def P3(world):
    '''
    world: M x N list, M>=1, N>=1
    '''
    '''
    아이디어 : 땅에 도착 = 방문한적 없고, 그 값이 1인경우
    논리 흐름은 대략 다음과 같음
    1. 모든 리스트 값에 대해 루프를 돌림
    2. 현재 인덱스가 1인지 + 방문한적 없는지 판별함
    3. 만약 위의 조건이 맞다면 땅이기 때문에 땅의 카운트를 더함
        3.1 해당 인덱스에서 인접한 인덱스가 땅인지, 물인지 판별함
        3.2 인접이 땅이라면 그 다음도 땅인지 판별함 (recursion)
        3.3 recursion을 통해 현재 밟은 땅에서 그곳에 연결된 땅(1)을 모두 판별함
    4. 다음 루프로 넘어감
    -> 3.1~3.3을 통해 만약 연결된 땅이라면 이미 visited = True로 바껴있음
    5. 모든 루프를 돌려 값을 찾음
    '''
    #m
    m = len(world[0])
    #n
    n = len(world)
    # 방문 판별용 딕셔너리
    visited = {}

    # 0,1의 모든 좌표를 dictionary에 더함
    # {0:[(3,3),(4,4),....],
    # 1:[{1,1},(2,6)....]
    # }
    # 모든 좌표도 visited = False로
    value_coord_dict = {}
    value_coord_dict[0] = []
    value_coord_dict[1] = []
    for i in range(n):
        for j in range(m):
            visited[(i, j)] = False
            value_coord_dict[world[i][j]].append((i, j))
    # landcount만듬
    landCount = 0

    #helper. 만약 현재 밟은 위치가 방문한적 없고, 땅이라면 visited를 True로 바꿈
    # 또한 해당 위치의 위,아래,왼쪽,오른쪽에 대해서도 마찬가지로 recursion을 통해 visited 반영함
    def p3Helper(value_coord_dict, visited, landCount, v, m, n):
        #방문한적 없고, 땅이라면
        if (visited[v] == False) and (v in value_coord_dict[1]):

            visited[v] = True
            # 위
            if (v[0]-1 >= 0):
                p3Helper(value_coord_dict, visited,
                        landCount, (v[0]-1, v[1]), m, n)
            # 아래
            if (v[0] + 1 < n):
                p3Helper(value_coord_dict, visited,
                        landCount, (v[0]+1, v[1]), m, n)
            # 왼쪽
            if (v[1] - 1 >= 0):
                p3Helper(value_coord_dict, visited,
                        landCount, (v[0], v[1]-1), m, n)
            # 오른쪽
            if (v[1] + 1 < m):
                p3Helper(value_coord_dict, visited,
                        landCount, (v[0], v[1]+1), m, n)


    #큰 루프. 전체에 대해서 돈다
    for i in range(n):
        for j in range(m):
            # 현재 밟은 곳이 땅이고 밟은적 없다면
            if (world[i][j] == 1) and (visited[(i,j)] == False):
                # 대륙갯수에 하나 더한다
                landCount += 1
                # 현재 위치 주변이 땅인지 판별한다.Helper
                p3Helper(value_coord_dict,visited,landCount,(i,j),m,n)


    return landCount