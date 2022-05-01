# 23253 자료구조는 정말 최고야

# by oneself
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stack = []

cnt = 0
for i in range(M):
    pile_number = int(input()) # 더미의 개수가 몇 개인지
    pile = list(map(int, input().split()))
    is_sorted = all(pile[j] > pile[j+1] for j in range(len(pile)-1))
    if not is_sorted:
      cnt += 1

print("Yes" if cnt == 0 else "No")

