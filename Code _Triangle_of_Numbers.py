## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i <= n:
    spaces = n - i
    for _ in range(0, spaces):
        print(" ", end='')

    j = 1
    starting_term = i
    middle_term = ((i * 2) - 1) - starting_term + 1
    while j <= (i * 2) - 1:
        if j == 1:
            print(starting_term, end='')
        elif j > middle_term:
            starting_term = starting_term - 1
            print(starting_term, end='')
        else:
            starting_term = starting_term + 1
            print(starting_term, end='')
        j = j + 1
    print()
    i = i + 1