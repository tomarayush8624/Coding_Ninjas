n = int(input())
# row number
i = 1
while i <= n:
    # column number
    j = 1
    while j <= (n - i) + 1:
        print(i % 2, end="")
        j = j + 1

    # next line
    print()

    # next row
    i = i + 1