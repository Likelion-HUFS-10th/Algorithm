'''
양뱡향 순환 큐 ..?
deque 모듈 사용 -> 구글 검색 찬스...
deque 메서드 -> appendleft(), popleft(), rotate()..

'''

from collections import deque

n, m = map(int,input().split())
num = list(map(int,input().split()))               # 수의 위치 입력 받기
queue = deque(range(1,n+1))                        # 다른 풀이 참고

cnt = 0

for i in num:
    while True:
        if queue[0] == i:     
            queue.popleft()
            break
        else:
            if queue.index(i) <= len(queue) / 2:    
                queue.rotate(-1)                    # rotate(입력값) -> 입력값 만큼 이동 -> 양수면 오른쪽 , 음수는 왼쪽으로 이동
                cnt += 1 
            else:
                queue.rotate()                       
                cnt += 1                          

print(cnt)



