## Read input as specified in the question
## Print the required output in given format
n = int(input())
for i in range (n):
    cur_column = i
    for j in range(i+1):
        print(chr(cur_column + 65), end='')
        cur_column = cur_column + 1
    print()
    i = i + 1