## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

# Part 01
n1 = (n + 1) / 2

i = 1
while i <= n1:
    spaces = int(n1 - i)
    for _ in range(0, spaces):
        print(" ", end='')

    j = 1
    while j <= (2 * i - 1):
        print("*", end="")
        j = j + 1

    print()
    i = i + 1

n2 = n1 - 1

i1 = 1
while i1 <= n2:
    spaces1 = int(i1)
    for _ in range(0, spaces1):
        print(" ", end="")

    j1 = 1
    while j1 <= (n - 2 * i1):
        print("*", end="")
        j1 = j1 + 1

    print()
    i1 = i1 + 1