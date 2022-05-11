import sys
input = sys.stdin.readline

def Tree(start, end, n):
    if start == end:
        tree[n].append(num_list[start])
        return
    mid = (start + end) // 2
    tree[n].append(num_list[mid])
    Tree(start, mid-1, n+1)
    Tree(mid+1, end, n+1)


k = int(input())
tree = [[] for _ in range(k)]
num_list = list(map(int, input().split()))
len_num = len(num_list)

Tree(0, len_num-1, 0)
for i in range(k):
    for j in tree[i]:
        print(j, end=' ')
    print()