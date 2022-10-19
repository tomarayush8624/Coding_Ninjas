## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= ((n+1) - i):
        print(j, end='')
        j = j+1
    print()
    i = i + 1