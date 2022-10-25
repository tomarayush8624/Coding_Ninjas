import sys


def intersections(arr1, n, arr2, m):
    # Your code goes here
    value = ""

    for i in arr1:
        flag = False
        for j in arr2:
            if i == j:
                str1 = i
                value = value + str(str1) + " "
                flag = True
                break
        if flag:
            arr2.remove(i)

    print(value)


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(sys.stdin.readline().strip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1