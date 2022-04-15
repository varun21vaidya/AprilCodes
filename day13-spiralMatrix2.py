# https://leetcode.com/problems/spiral-matrix-ii/

def generateMatrix(n):
    #         x,y=0,-1
    #         row,col,dirr=n,n,1

    #         mat=[[None for i in range(n)] for i in range(n)]
    #         value=1
    #         while row>0 and col>0:
    #             for i in range(col):
    #                 y+=dirr
    #                 mat[x][y]=value
    #                 value+=1
    #             row-=1

    #             for i in range(row):
    #                 x+=dirr
    #                 mat[x][y]=value
    #                 value+=1
    #             col-=1

    #             dirr*=-1

    #         return mat

    m = n  # rows
    n = n  # column
    value = 1
    matrix = [[None for i in range(n)] for i in range(m)]
    startm, endm = 0, m
    startn, endn = 0, n
    while startm < endm and startn < endn:
        for i in range(startn, endn):  # moving left to right through column
            matrix[startm][i] = value  # row will be decided by startm ie top
            value += 1
        startm += 1  # top row will move downward to crop the matrix
        for i in range(startm, endm):  # moving top to bottom through m rows
            # column will be const and is right end endn, and to avoid out of bound index -1
            matrix[i][endn-1] = value
            value += 1
        endn -= 1  # matrix be cropped by shifting rightmost end towards left

        for i in range(endn-1, startn-1, -1):  # moving right to left through column
            matrix[endm-1][i] = value  # row will be decided by endm ie bottom
            value += 1
        endm -= 1  # bottom row will move upward to crop the matrix
        for i in range(endm-1, startm-1, -1):  # moving bottom to top through m rows
            # column will be const and is left end startn
            matrix[i][startn] = value
            value += 1
        startn += 1  # matrix be cropped by shifting leftmost end towards right

    return matrix


print(generateMatrix(3))
