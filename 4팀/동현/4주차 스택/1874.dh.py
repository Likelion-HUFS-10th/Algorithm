"""
result_list에 +,- 추가
stack 리스트에서 확인하는 방법
"""
import sys
n = int(input())
num_list = [
    int(input())
    for _ in range(n)
]

stack = []
result_list = []
num = 1

for i in num_list:
    while i >= num:
        stack.append(num)
        result_list.append('+')
        num += 1
    if stack[-1] == i:
        stack.pop()
        result_list.append('-')
    else:
        print('NO')
        sys.exit()

for j in result_list:
    print(j)

