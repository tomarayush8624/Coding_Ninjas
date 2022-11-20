from sys import stdin


def reverseEachWord(string):
    # Your code goes here
    new_list = string.split(' ')
    # print(new_list)
    answer = ""
    for word in new_list:
        for reversed_word in range(len(word) - 1, -1, -1):
            answer += word[reversed_word]

        answer += " "
    return answer


# main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)