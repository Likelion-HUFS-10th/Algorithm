import sys
input = sys.stdin.readline
HEIGHT, CNT = 0, 1

N  = int(input())
arr = [int(input()) for _ in range(N)]
stack = [] # 비교 대상을 내림차순으로 유지하는 스택
answer = 0
for a in arr:
    while stack and stack[-1][HEIGHT] < a:  # a가 stack 내에 있는 마지막 사람보다 큰 경우 (마지막 사람과 서로 볼 수 있음)
        answer += stack.pop()[CNT] # 그 수를 더해주고 stack에서 제거해줌 

    if not stack:
        stack.append((a, 1))

    elif stack[-1][HEIGHT] == a:  #같은 키인 사람이 마지막에 있다면
        cnt = stack.pop()[CNT]
        answer += cnt
        if stack : #stack 내에서 가장 큰 사람과 서로 볼 수 있음.
            answer += 1
        stack.append((a, cnt + 1)) # stack에 a 추가

    else: # stack[-1][HEIGHT] > a 인 경우
        stack.append((a, 1))
        answer += 1 # stack 내에 가장 마지막에 있던 사람과 a만 볼 수 있음
print(answer)
