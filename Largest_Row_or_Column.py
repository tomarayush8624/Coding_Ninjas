'''
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin


def findLargest(arr, nRows, mCols):
    # Your code goes here

    # largest sum in each row
    r_largest = 0

    for i in range(nRows):
        r_sum = 0
        for j in range(mCols):
            r_sum = r_sum + arr[i][j]
        if r_largest < r_sum:
            r_largest = r_sum
            r_index = i

    # largest sum of each column
    c_largest = 0
    for column in range(mCols):
        c_sum = 0
        for row in range(nRows):
            c_sum = c_sum + arr[row][column]
        if c_largest < c_sum:
            c_largest = c_sum
            c_index = column

    if r_largest == 0 and c_largest == 0:
        print("row 0 -2147483648")
    elif r_largest == c_largest:
        print("row " + str(r_index) + " " + str(r_largest))
    else:
        if r_largest > c_largest:
            print("row " + str(r_index) + " " + str(r_largest))
        else:
            print("column " + str(c_index) + " " + str(c_largest))


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
    findLargest(mat, nRows, mCols)

    t -= 1