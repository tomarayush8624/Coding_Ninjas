import sys


def duplicateNumber(arr, n):
    # Your code goes here
    #     dummy_lst = []
    #     for i in range(0, (n - 2)):
    #         dummy_lst.append(i)
    count = 0
    for j in arr:
        count_2 = 0
        for k in arr:

            if count != count_2:
                if j == k:
                    return j
            count_2 += 1
        count += 1


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


# main
t = int(sys.stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1
