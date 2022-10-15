## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

# Row Count
i = 1

while i <= n:
    # column count for part 1 of problem
    j1 = 1
    while j1 <= n:
        if j1 == i:
            print("*", end="")
        else:
            print("0", end="")
        j1 = j1 + 1

    print("*", end="")

    # column count for part 2 of the problem
    #    print(j1)
    j2 = 1
    while j2 <= n:
        if j2 == (n - i + 1):
            print("*", end="")
        else:
            print("0", end="")
        j2 = j2 + 1

    # next line
    print()

    # next row
    i = i + 1