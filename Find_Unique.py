import sys

def findUnique(arr, n) :
    #Your code goes here
    for i in range(0, n, 1):
        count = 0
        for j in range(0, n, 1):
            if arr[i] == arr[j]:
                count = count + 1
        if count == 1:
            return arr[i]

#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1