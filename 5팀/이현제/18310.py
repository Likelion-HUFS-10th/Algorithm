import collections

n = int(input())
arr = list(map(int,input().split()))
avg = sum(arr)/n

dic = {}
for i in arr:
    dic[i] = abs(avg - i)

dic = sorted(dic.items(), key=lambda x: x[1])

print(dic[0][0])