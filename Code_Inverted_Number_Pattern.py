## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while i <= n:
    j = 1
    cur_val = n + 1 - i
    while j <= cur_val:
        print(cur_val, end='')
        j = j + 1
    print()
    i = i + 1