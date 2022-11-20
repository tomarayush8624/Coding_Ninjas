from sys import stdin


def removeConsecutiveDuplicates(string):
    # Your code goes here
    new_str = ""
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            continue
        else:
            new_str += string[i]

    new_str += string[len(string) - 1]
    return new_str


# main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)