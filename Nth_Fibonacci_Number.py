## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
num = [1, 1, 2]
fibonacci_no = 3

while n > fibonacci_no:
#    num[fibonacci_no + 1] = (num[fibonacci_no] + num[fibonacci_no - 1])
    num.append(num[fibonacci_no - 1] + num[fibonacci_no - 2])
    fibonacci_no = fibonacci_no + 1

print(num[n- 1])
