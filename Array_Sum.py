## Read input as specified in the question.
## Print output as specified in the question.

# toatal number of test cases
n = int(input())
ary = map(int, input().split())
sum = 0
for i in ary:
    sum = sum + i
print(sum)