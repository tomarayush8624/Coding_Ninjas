def checkPalindrome(num):
    # Implement Your Code Here
    marker = num
    rev = 0
    while marker > 0:
        rev = (marker % 10) + (rev * 10)
        marker = marker // 10
    if rev == num:
        return True
    else:
        return False


num = int(input())
isPalindrome = checkPalindrome(num)
if (isPalindrome):
    print('true')
else:
    print('false')
