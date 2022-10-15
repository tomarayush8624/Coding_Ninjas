# input number of rows assuming them as odd every time
n = int(input())

# Calculating number of times part 1 of problem should run
n1 = int((n + 1) / 2)

i1 = 1
while i1 <= n1:
    # Print Spaces
    spaces = i1 - 1
    for _ in range(0, spaces):
        print(" ", end="")

    # Print Pattern
    j1 = 1
    while j1 <= i1:
        print("*", end="")
        print(' ', end="")
        j1 = j1 + 1

    # Shifting to new line
    print()
    i1 = i1 + 1

# Printing Seacond Part of Pattern

n2 = n1 - 1
i2 = 1

while i2 <= n2:
    # Print Spaces
    spaces_2 = (n2 - i2)
    for _ in range(spaces_2):
        print(" ", end="")

    # Print Pattern
    j2 = 1
    while j2 <= (n2 - i2) + 1:
        print("*", end="")
        print(" ", end="")
        j2 = j2 + 1

    # Print new Line
    print()

    i2 = i2 + 1
