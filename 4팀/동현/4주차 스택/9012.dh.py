
"""
중간에 '('보다 ')'의 개수가 많아지는 경우
스택인지..??
"""
n = int(input())
bracket_list = [
    input()
    for i in range(n)
]

for j in bracket_list:
    sum = 0
    for k in j:
        if k == '(':
            sum += 1
        elif k == ')':
            sum += -1
        if sum < 0:
            print('NO')
            break
    if sum == 0:
        print('YES')
    elif sum > 0:
        print('NO')