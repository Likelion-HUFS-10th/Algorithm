"""
정수를 저장하는 스택, 명령을 입력받음
명령은 n개 입력 받음 => 명령 + 숫자 형식 고려 by split()
"""
n = int(input())
order_list = [
    tuple(input().split())
    for _ in range(n)
] # 리스트 내부 for문 사용

result = []

for i in order_list:
    if i[0] == 'push':
        result.append(i[1])
    elif i[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif i[0] == 'size':
        print(len(result))
    elif i[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])