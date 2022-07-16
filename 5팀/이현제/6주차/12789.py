from collections import deque

a = int(input())
current = deque(map(int, input().split()))
cnt = 1 
solo_count = 0  # 한줄로 서있는 스택의 개수
while cnt < a:
    if solo_count != len(current) and current[0] == cnt:
        current.popleft()
        cnt += 1
    elif solo_count >= 1 and current[-1] == cnt:
        current.pop()
        solo_count -= 1
        cnt += 1
    else:
        if solo_count == len(current):
            if current[-1] != cnt:
                print('Sad')
                break
        current.rotate(-1)
        solo_count += 1
if cnt == a:
    print('Nice')