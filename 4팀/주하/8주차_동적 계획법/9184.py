'''

DP 동적 계획법 해결 방법 => 1. 재귀함수 2. for문

재귀함수 메모이제이션 사용(중복 제거)

'''
import sys

memo = [[[0]* 21 for _ in range(21)] for _ in range(21)]   # a,b,c 변수 3개 -> 3차원 배열 만들어서 0으로 초기화

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c >20:
        return w(20, 20, 20)
    if memo[a][b][c] != 0 :             # 이미 구했다면 있는 값 그대로 반환(중복확인)
        return memo[a][b][c]
    if a < b < c :
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]               # 재귀
    else:
        memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[a][b][c]               # 재귀


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    else:
        print(f'w{a,b,c} = {w(a,b,c)}')
