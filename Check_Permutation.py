from sys import stdin


def sorted_str(input_str):
    '''This Function returns the string with each character in its alphabetical order'''
    new_str = "".join(sorted(input_str))
    return new_str


def isPermutation(string1, string2):
    # Your code goes here
    if len(string1) != len(string2):
        return False

    string1 = sorted_str(string1)
    string2 = sorted_str(string2)

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    return True


# main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans:
    print('true')
else:
    print('false')

