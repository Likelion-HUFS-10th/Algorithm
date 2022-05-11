"""
deque 사용
큐를 만드는 법..?? > 구글링 참고
연산의 최솟값 > 큐에서의 위치에 따라 빼주는 것을 다르게
구글링으로 이해하는 수준...
"""
from collections import deque

n,m = map(int,input().split())
num = list(map(int,input().split()))

que = deque(range(1,n+1))   
result = 0

for i in num:
    while True: # 뽑힐 때까지 반복
        if que[0] == i: # que의 첫 인덱스가 수의 위치와 같을 때 => 0번
            que.popleft()
            break
        else:
            if que.index(i) < len(que)/2: # 왼쪽에서 접근하는게 최소일 때
                while que[0] != i: # 둘이 같아질 때까지 반복(위의 조건)
                    que.append(que.popleft())
                    result += 1
            else: # 오른쪽에서 접근하는게 최소일 때
                while que[0] != i: # 둘이 같아질 때까지 반복(위의 조건)
                    que.appendleft(que.pop()) 
                    result += 1
print(result)