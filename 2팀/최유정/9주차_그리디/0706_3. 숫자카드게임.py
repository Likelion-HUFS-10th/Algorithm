n, m = map(int, input().split())
card = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = []
max_num = 0
for i in card:
    min_num = min(i)
    max_num = max(min_num, max_num)

print(max_num)