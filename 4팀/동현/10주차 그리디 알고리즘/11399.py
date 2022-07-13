"""
값을 오름차순으로 정렬하여 해결
하나씩 계속 더해주는 방법 사용
"""
N = int(input())

num_list = list(map(int,input().split()))
num_list.extend([0])

num_list.sort()

result = 0

for i in range(N+1):
    for j in range(i+1):
        result += num_list[j]
        
print(result)