"""
단순 재귀로는 시간초과..
메모제이션 기법 사용
리스트로 담는 방법은 이해x
딕셔너리로 담는 방법 사용
"""
import sys

w_dict = {}

def w(a,b,c):
    if (a,b,c) in w_dict:
        return w_dict[(a,b,c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            w_dict[(a,b,c)] = 1
            return 1
        if a > 20 or b > 20 or c > 20:
            w_dict[(a,b,c)] = w(20,20,20)
            return w(20, 20, 20)
        if a < b and b < c:
            w_dict[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            w_dict[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
 
while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')