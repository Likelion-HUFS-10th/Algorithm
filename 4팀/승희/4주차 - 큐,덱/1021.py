from collections import deque

n,m = map(int,input().split())
del_arr = list(map(int,input().split())) #빼고싶은 수의 위치
arr= [i for i in range(1,n+1)] #큐
dq = deque(arr)

head_idx = 0 #인덱스는 0부터 시작
cnt=0

for num in del_arr:
    while True:
        if dq[0]==num:
            dq.popleft()
            break
        else:
            if dq.index(num) > len(dq)/2:
                while dq[0]!=num:
                    dq.appendleft(dq.pop()) #뒤쪽에 있으면 뒤를 계속 pop해서 앞에 append
                    cnt+=1
            else:
                while dq[0]!=num:
                    dq.append(dq.popleft()) #앞에 있으면 앞을 계속 pop 하고 뒤에 계속 append
                    cnt+=1

print(cnt)