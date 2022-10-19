def checkPalindrome(num):
    pali_num = 0
    real_num = num
    for i in range(1, len(str(num)) + 1, 1):
        last_digit = real_num % 10
        pali_num = (pali_num * 10) + last_digit
        real_num = real_num // 10
    if pali_num == num:
        return True
    else:
        return False


num = int(input())
isPalindrome = checkPalindrome(num)
if (isPalindrome):
    print('true')
else:
    print('false')
