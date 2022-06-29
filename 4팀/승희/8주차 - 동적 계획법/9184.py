'''
a,b,c 중에 0보다 작거나 같은 수가 있으면 1을 반환
a,b,c 중에 20보다 큰 수가 있으면 재귀적으로 w(20,20,20) 호출
a가 b보다 작고 c보다 b가 작으면 (a<b, b<c) w(a,b,c-1)+w(a,b-1,c-1) - w(a,b-1,c)
그 무엇도 아닌 경우에는 w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''

#0보다 작으면 무조건 1이고, 20보다 크면 무조건 20 => -50~50이지만 사실상 0부터 20까지만 필요!
dp = [
    [[0 for _ in range(21)] for _ in range(21)] for _ in range(21)
]


def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a<b<c:
        dp[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
