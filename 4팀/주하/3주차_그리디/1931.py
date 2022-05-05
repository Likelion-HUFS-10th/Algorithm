n = int(input())

conf = [ list(map(int,input().split())) for _ in range(n) ]
conf.sort(key=lambda x: (x[1],x[0]))     # 끝나는 시간으로 정렬, 시작 시간으로 정렬

cnt = 1 
last_end = conf[0][1]

for i in range(1,n):
    if last_end <= conf[i][0]:     # 겹치지 않는 회의 시간 (시작 시간이 이전 회의 끝나는 시간 보다 크거나 같은 경우)
        last_end = conf[i][1]      # 해당 회의 선택
        cnt += 1

print(cnt)
