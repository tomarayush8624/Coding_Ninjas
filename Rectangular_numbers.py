## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())


l= n
for i in range(n):
    space=n
    for j in range(i):
        print(space, end='')
        space-=1
    for k in range(2*(n-i)-1):
        print(l, end='')
    for j in range(i):
        space+=1
        print(space, end='')
    print()
    l-=1
for i in range(n):
    l+=1
    space =n
    if (i==0): continue
    for j in range(n-i-1):
        print(space, end='')
        space-=1
    for k in range(2*i+1):
        print(l, end='')
    for j in range(n-i-1):
      space+=1
      print(space,end='')
    print()