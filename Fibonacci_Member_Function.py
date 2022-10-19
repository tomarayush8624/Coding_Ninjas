
def checkMember(n):
    '''This Functon return true if the number is in fibbonacci series else returns false'''
    # Fibonaci num list
    fib_lst = [0, 1, 1, 2]
    # we will add new items in this list and check if n is equal to them
    check = False
    for i in range(1, n+1, 1):
        fib_num = fib_lst[i-1] + fib_lst[i]
        if n == fib_num:
            return True
            break
        else:
            if i > 2:
                fib_lst.append(fib_num)
        if fib_num > n:
            return False
            break
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")