from sys import stdin


def rowWiseSum(mat, nRows, mCols):
    # Your code goes here
    # print(mat)
    # print(mat[0])
    for i in range(0, nRows):
        sum = 0
        for j in range(mCols):
            sum = sum + mat[i][j]
        print(sum, end=" ")


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    rowWiseSum(mat, nRows, mCols)
    print()

    t -= 1