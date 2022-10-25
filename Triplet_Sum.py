from sys import stdin


def pairSum(arr, n, x):
    # Your code goes here
    pairs = 0
    for i in arr:
        flag = False
        for j in arr:
            if (i + j == x):
                pairs = pairs + 1
                flag = True
        if flag:
            continue
    return (pairs // 2)


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1