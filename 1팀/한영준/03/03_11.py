import sys
n,x = map(int,sys.stdin.readline().split())
list_a = list(map(int,sys.stdin.readline().split()))
list_b = []
for i in range(len(list_a)):
    if list_a[i] < x :
        list_b.append(list_a[i])

for k in list_b :
    print(k, end=' ')