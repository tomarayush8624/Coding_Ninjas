## Read input as specified in the question.
## Print output as specified in the question.
def check_armstrong(n):
    arm_num = 0
    dummy = n
    dgts = len(str(n))
    for i in range(0, dgts, 1):
        last_dgt = dummy % 10
        arm_num = arm_num + (last_dgt ** int(dgts))
        dummy = dummy // 10

    if arm_num == n:
        return True
    else:
        return False


n = int(input())
if check_armstrong(n):
    print("true")
else:
    print("false")