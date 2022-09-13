# 리스트 돌면서 앞쪽 숫자랑 비교

n = int(input())
a = list(map(int, input().split()))
d = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))


# n = int(input())
# a = list(map(int,input().split()))
# a_set = set(a)
# a_list = sorted(a_set,reverse=True)
# print(len(a_list))
