n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        if i == 2:
            print(i-1, end='')
        elif i == 1:
            print(i, end='')
        elif j == 1:
            print(i-1, end='')
        elif j == i:
            print(i-1, end='')
        else:
            print(0, end='')
        j = j + 1
    print()
    i = i + 1