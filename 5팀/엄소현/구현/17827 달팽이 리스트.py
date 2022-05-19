import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())   # n: 노드 개수, m: 질문 횟수, v: 노드 n이 가리키는 노 번호
l = list(map(int, input().split()))   # 노드 정수

for _ in range(m):
    k = int(input())   # 이동하려는 노드 칸 수
    if k - 1 < n - 1:
        print(l[k])
    else:
        left = k - n   # v로 돌아옴
        left = left % (n - v + 1)
        print(l[v-1+left])
