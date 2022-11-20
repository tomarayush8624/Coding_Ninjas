n = int(input())
i = 1
while i <= n:
    # Part 1
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    count = i
    spaces = int(n - i)
    for _ in range(0, spaces):
        print(" ", end="")

    spaces_1 = int(n - i)
    for _ in range(0, spaces_1):
        print(" ", end="")
    j1 = count
    j2 = 1
    while j2 <= i:
        print(j1, end="")
        j1 = j1 - 1
        j2 = j2 + 1

    print()
    i = i + 1