def P3(matrix):

    # select diagonal
    # matrix[i][0], matrix[i+1][1],...,matrix[i+j][j]
    n = len(matrix)
    m = len(matrix[0])
    #base case
    if (m == 1) or (n == 1):
        return matrix
    # Traverse vertical first
    #matrix[0][0],matrix[1][1],...,matrix[n][n]
    # i+j < n, j < m
    for i in range(n-1):
        #swap
        swap = True
        while swap == True:
            swap = False
            for j in range(m-1):
                if (i+j == n -1):
                    break
                if matrix[i+j][j] > matrix[i+j+1][j+1]: 
                    swap = True
                    temp = matrix[i+j][j]
                    matrix[i+j][j] =  matrix[i+j+1][j+1]
                    matrix[i+j+1][j+1] = temp
    
    # Traverse horizontal
    for i in range(1,m-1):
        #swap
        swap = True
        while swap == True:
            swap = False
            for j in range(n-1):
                if (i+j == m - 1):
                    break
                if matrix[j][i+j] > matrix[j+1][i+j+1]: 
                    swap = True
                    temp = matrix[j][i+j]
                    matrix[j][i+j] =  matrix[j+1][i+j+1]
                    matrix[j+1][i+j+1] = temp
    # sort diagnoal
    return matrix
print(P3([[5,5,5,5],[1,2,6,4],[2,3,90,12],[17,12,89,78]]))