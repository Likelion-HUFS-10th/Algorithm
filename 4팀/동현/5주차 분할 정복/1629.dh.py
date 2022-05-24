"""
지수를 이용하는 방법
지수가 짝수일 때와 홀수일 때 구분
"""
import sys
A,B,C = map(int, sys.stdin.readline().split())

def multiple_num(A,B):
    if B == 1:
        return  A % C
    
    else:
        new = multiple_num(B // 2)
        if B % 2 == 0:
            return new * new % C

        else:
            return new * new * A % C

print(multiple_num(A,B))

    



