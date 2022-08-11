from itertools import permutations

N = int(input())
num_lst = list(map(int, input().split()))
operators = list(input().split())
ops = ['+', '-', '*', '//']

final = []
for i in range(4):
    for j in range(int(operators[i])):
        final.append(ops[i])

final = [w for w in final if w != '']
max = -10**9
min = 10**9

for c in permutations(final, N-1):
    answer = num_lst[0]
    for i in range(1, N):
        if c[i-1] == "+":
            answer += num_lst[i]
        elif c[i-1] == '-':
            answer -= num_lst[i]
        elif c[i-1] == '*':
            answer *= num_lst[i]
        elif c[i-1] == '//':
            if answer < 0:
                answer = -(abs(answer) // num_lst[i])
            else:
                answer //= num_lst[i]
    if answer > max:
        max = answer
    if answer < min:
        min = answer

print(max)
print(min)



