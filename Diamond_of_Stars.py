## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
n1 = int((n + 1) / 2)
n2 = n1 - 1

# Part 1 of the problem
for i in range(0, n1, 1):

    # Printing Spaces
    spaces_1 = n1 - (i + 1)
    for _ in range(0, spaces_1, 1):
        print(" ", end="")

    # printing stars
    num_of_col = (i * 2) + 1
    for _ in range(0, num_of_col, 1):
        print("*", end="")
    print()

# Part 2 of th problem
for i2 in range(0, n2, 1):

    # Printing Spaces
    spaces_2 = i2 + 1
    for _ in range(0, spaces_2, 1):
        print(" ", end="")

    # Printing Stars
    num_of_col_2 = n - (i2 + 1) * 2
    for _ in range(0, num_of_col_2, 1):
        print("*", end="")

    # Print new line
    print()