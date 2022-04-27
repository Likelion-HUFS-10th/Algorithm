import math
n, m = map(int, input().split())
list_num = list(map(int, input().split()))
result = 0
for i in range(len(list_num)):
    for j in range(i+1,len(list_num)):
        for t in range(j+1, len(list_num)):
            if list_num[i] + list_num[j] + list_num[t] > m:
                continue
            else:
                result = max(result, list_num[i]+list_num[j]+list_num[t])
print(result)