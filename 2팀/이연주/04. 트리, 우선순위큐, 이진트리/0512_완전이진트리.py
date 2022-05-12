import sys
input = sys.stdin.readline
k = int(input())
nodes = list(map(int, input().split()))
n = len(nodes)
tree = [[] for _ in range(k)]

def solution(start, end, level):
    global tree, nodes
    if start == end:
        tree[level].append(nodes[start])
        return
    mid = (start + end) // 2
    tree[level].append(nodes[mid])
    solution(start, mid-1, level+1)
    solution(mid+1, end, level+1)

solution(0, n-1, 0)
for t in tree:
    print(*t)