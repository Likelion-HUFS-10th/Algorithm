n = int(input()) #사람의 수
times = list(map(int,input().split()))

times.sort()
result = 0
current_time = 0

for time in times:
    current_time += time
    result += current_time

print(result)