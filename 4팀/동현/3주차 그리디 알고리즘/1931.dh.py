"""
시작 시간과 끝나는 시간을 기준으로 정렬
finish_time을 갱신하며 count를 최대화
"""
N = int(input())
time_list = []
for i in range(N):
    time_list.append(tuple(map(int,input().split())))

time_list = sorted(time_list, key = lambda x:x[0])
time_list = sorted(time_list, key = lambda x:x[1])
finish_time = time_list[0][1]
count = 1

for i,j in time_list:
    if i >= finish_time:
        finish_time = j
        count += 1
print(count)