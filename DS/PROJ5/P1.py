def P1(room):
    '''
    room: M x N list, M>=1, N>=1
    '''
    #m
    m = len(room[0])
    #n
    n = len(room)
    V = {}
    #각 value와, 이에 대응하는 좌표들 딕셔너리. 1:[(1,4),(2,5)....]
    value_coord_dict = {}
    #방문 딕셔너리. (좌표), Boolean pair
    visited = {}
    #1갯수 계산. while loop에서 1갯수가 증가하지 않으면 break
    one_count_old = 0
    # 0 갯수. 나중에 0갯수가 0이 아니면 -1 return
    zero_count = 0
    # m * n 루프
    for i in range(m):
        for j in range(n):
            # 모든 좌표 visited false
            visited[(j, i)] = False
            V[(j, i)] = room[j][i]
            # 각 value(1,0,-1)과 대응하는 좌표 리스트 만들기
            value_coord_dict.setdefault(room[j][i], [])
            value_coord_dict[room[j][i]].append((j, i))

            # 1 갯수 더하기
            if room[j][i] == 1:
                one_count_old += 1
            #0 갯수 더하기
            if room[j][i] == 0:
                zero_count += 1
    #while loop가 몇번 돌아갔는지 저장할 변수
    count = 0

    # 1갯수 
    one_count = 0


    while one_count_old - one_count != 0:
        one_count_old = one_count
        #1만 들어있는 dict.{1:[(3,4),(2,1)...]}
        one_coord_list = value_coord_dict[1].copy()
        for coordinate in one_coord_list:
            # 일단 1인 좌표는 다 꺼내기 때문에, 이 중에 아직 방문하지 않은 1을 대상으로 계산
            if visited[coordinate] == False:
                #해당 루프에서 아직 방문하지 않은 1들
                visited[coordinate] = True
                # 위, 해당 좌표의 위가 0 이면, 1로 바꾸고, 딕셔너리에 좌표 저장, 0-> 1로 바뀌니 0갯수 감소, 1 갯수 증가
                if (coordinate[0]-1 >= 0):
                    if room[coordinate[0]-1][coordinate[1]] == 0:
                        room[coordinate[0]-1][coordinate[1]] = 1
                        value_coord_dict[1].append((coordinate[0]-1,coordinate[1]))
                        one_count += 1
                        zero_count -= 1
                # 아래
                if (coordinate[0]+1 < n):
                    if room[coordinate[0]+1][coordinate[1]] == 0:
                        room[coordinate[0]+1][coordinate[1]] = 1
                        value_coord_dict[1].append((coordinate[0]+1,coordinate[1]))
                        one_count += 1
                        zero_count -= 1
                # 왼쪽
                if (coordinate[1]-1 >= 0):
                    if room[coordinate[0]][coordinate[1]-1] == 0:
                        room[coordinate[0]][coordinate[1]-1] = 1
                        value_coord_dict[1].append((coordinate[0],coordinate[1]-1))
                        one_count += 1
                        zero_count -= 1
                # 오른쪽
                if (coordinate[1]+1 < m):
                    if room[coordinate[0]][coordinate[1]+1] == 0:
                        room[coordinate[0]][coordinate[1]+1] = 1
                        value_coord_dict[1].append((coordinate[0],coordinate[1]+1))
                        one_count += 1
                        zero_count -= 1
        # 만약 1갯수의 변화가 없다면, 루프 멈춤
        if one_count_old == one_count:
            break
        # count더함
        count += 1
    #0이 아직 남아있다면 -1 return
    if zero_count != 0:
        return -1
    #아니면 그냥
    return count
 
