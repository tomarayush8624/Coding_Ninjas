## Read input as specified in the question.
## Print output as specified in the question.

n =int(input())
i = 1
while i <= n:
    j = 1
    spaces = n - i
    while j <= n + i -1:
        if j in range (0, spaces+1):
            print(" ", end='')
        else:
            print("*", end='')
        j = j + 1
    print()
    i = i + 1