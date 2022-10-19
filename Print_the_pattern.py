n = int(input())

# Sorting Odd and even numbers and assigning Rows
if n % 2 == 0:
    n1 = (n // 2)
    n2 = n - n1
else:
    n1 = (n + 1) // 2
    n2 = n1 - 1

# Part 1 of the problem
for i in range(0, n1, 1):
    start = 1 + (i * (n * 2))
    for j in range(0, n, 1):
        print(start, end=" ")
        start = start + 1
    print()

    # Part 2 of the problem
for i2 in range(0, n2, 1):
    if n % 2 == 0:
        count = n - ((i2 * 2) + 1)
    else:
        count = n - (i2 + 1) * 2
    start_2 = n * (count) + 1
    for j2 in range(0, n, 1):
        print(start_2, end=" ")
        start_2 = start_2 + 1
    print()

