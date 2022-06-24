'''

백트래킹 -> 깊이우선탐색...

'''
n,m = map(int,input().split())
s = []

def DFS():
    if len(s) == m :
        print(' '.join(map(str,s)))      # 대괄호 제거해서 출력
        return

    for i in range(1,n+1):
        if i in s:                       # 중복 값 확인
            continue
        s.append(i)                     # 중복이 아니면 리스트에 값 추가
        DFS()
        s.pop()

DFS()
