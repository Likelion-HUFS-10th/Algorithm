import sys
input = sys.stdin.readline

n = int(input())
num_list = []
new_num_list = []
for i in range(n):
    num_list.append(i+1)
for _ in range(n-1):
    new_num_list.append(num_list.pop(0))
    num_list.append(num_list.pop(0))
lst = new_num_list + num_list
for i in range(len(lst)):
    print(lst[i], end=' ')