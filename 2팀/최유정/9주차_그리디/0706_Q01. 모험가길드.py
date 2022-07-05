n = int(input())
adv = list(map(int, input().split()))
adv.sort(reverse=True)
result = []
cnt = 0

while adv:
    per = adv.pop()
    result.append(per)
    if len(result) == per:
        cnt += 1
        result = []

print(cnt)