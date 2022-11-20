from sys import stdin


def isPalindrome(string):
    # Your code goes here
    reverse_string = string[::-1]
    # print(reverse_string)
    mark = True
    for count in range(0, len(string)):
        if string[count] != reverse_string[count]:
            # continue
            return False
    return mark


# main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans:
    print('true')
else:
    print('false')

