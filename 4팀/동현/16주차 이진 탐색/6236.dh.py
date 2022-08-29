"""
인출 횟수와 하루 사용하는 금액 모두 고려해야함
이분탐색을 이용하여 금액을 조정
"""
n, m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)

start = arr[0]
end = sum(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    money = mid
    count = 1
    for i in range(len(arr)):
        if arr[i] > money:
            money = mid
            count += 1
        money -= arr[i]

    if count <= m and mid >= max(arr):
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)