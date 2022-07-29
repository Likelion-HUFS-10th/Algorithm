"""
key의 모양을 바꾸는 방법으로 처음 접근 -> 잘못된 접근
하나의 solution 함수로 접근하려고 했지만 실패
키를 90도 회전시키는 rotate_key 함수
키와 lock이 맞는지 확인하는 checking 함수
key와 lock의 크기가 다를 수 있음을 인지
"""
def rotate_key(key):
    m = len(key)
    result = [[0]*m for _ in range(m)] # 90도 회전한 키의 모양을 담을 리스트
    for i in range(m):
        for j in range(m):
            result[j][m-i-1] = key[i][j] # 90도 회전시 키의 모양
    return result 

def checking(total):
    n = len(total) // 3 # 3으로 곱해줬기 때문
    for i in range(n, n*2):
        for j in range(n, n*2):
            if total[i][j] != 1: # 모두 1이 아닐 경우 -> 0 or 2 맞지 않음 => False
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    total = [[0] * (n*3) for _ in range(n*3)] # 키를 90도 회전했을 때 비교할 모든 lock들의 집합, 3을 곱하여 확장해줌
    
    for i in range(n):
        for j in range(n):
            total[i+n][j+n] = lock[i][j] # total에 lock의 값을 대입
    
    for _ in range(4): # 90도 4번
        key = rotate_key(key) # 회전한 키의 모습
        
        for a in range(2*n):
            for b in range(2*n):
                for i in range(m):
                    for j in range(m):
                        total[a+i][b+j] += key[i][j] # 해당부분에 키의 값을 더해줌 
        
                if checking(total): # total 전체에 대한 확인
                    return True
                
                for i in range(m):
                    for j in range(m):
                        total[a+i][b+j] -= key[i][j] # 원상복구
    return False

solution(key, lock)