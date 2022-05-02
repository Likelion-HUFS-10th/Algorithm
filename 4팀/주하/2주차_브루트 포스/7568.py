n = int(input())
state = []
for i in range (n):
    state.append(list(map(int,input().split())))   # [[w1,h1][w2,h2],[w3,h3].....] 형태로 입력 받기

for i in range (n):
    cnt= 1
    for j in range (n):                           # 전체를 돌면서 i보다 덩치 큰사람 있는지 확인
       if state[i][0] < state[j][0] and state[i][1] < state[j][1]:
           cnt +=1
    print(cnt, end=" ")
