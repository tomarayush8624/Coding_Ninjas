## Read input as specified in the question
## Print the required output in given format
n = int(input())
for i in range(n):
    j = 0
    while j <= i:
        print((i+1) - j, end='')
        j = j + 1
    print()