n = int(input())
i = 1
while i <= n:
    spaces = n - i
    j = 1
    while j <= n:
        if j in range(0, spaces+1):
            for _ in range(spaces):
                print(" ", end=(''))
        else:
            print(j - spaces, end='')
        j = j + 1
    print()
    i = i + 1