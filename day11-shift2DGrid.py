# https://leetcode.com/problems/shift-2d-grid/

def shiftGrid(grid, k):

    # Runtime: 144 ms, faster than 100.00% of Python3 online submissions for Shift 2D Grid.
    # Memory Usage: 14.4 MB, less than 13.09% of Python3 online submissions for Shift 2D Grid.

    # n=len(grid[0])
    # one=[j for i in grid for j in i ]
    # for repeat in range(k):
    #     one.insert(0,one.pop())
    # return [one[i:i+n] for i in range(0,len(one),n)]

    m = len(grid)
    n = len(grid[0])
    k = k % (m*n)
    one = [j for i in grid for j in i]
    one = one[-k:]+one[:-k]
    return [one[i:i+n] for i in range(0, len(one), n)]


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
print(shiftGrid(grid, k))
