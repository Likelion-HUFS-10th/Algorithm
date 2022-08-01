def match(arr, key, rot, row, col):    # 매칭 확인 함수
    n = len(key)
    for i in range(n):
        for j in range(n):
            if rot == 0:   # 회전 x -> 그대로 복사
                arr[row + i][col + j] += key[i][j]
            elif rot == 1:   # 90도 회전
                arr[row + i][col + j] += key[n-1 -j][i]
            elif rot == 2:   # 180도 회전
                arr[row + i][col + j] += key[n-1 -i][n-1 -j]
            else:            # 반시계 90도 회전
                arr[row + i][col + j] += key[j][n-1 -i]


def check(arr, offset, n):    # 자물쇠 1인지 아닌지 확인하는 함수
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:  # 자물쇠 영역 확인하기
                return False
    return True 

def solution(key, lock):
    offset = len(key) - 1

    for row in range(offset + len(lock)):    # 열쇠를 복사하기 위한 행,열, 전체 초기화, 가운데 자물쇠 복사
        for col in range(offset + len(lock)):
            for rot in range(4):
                arr = [[0] * (len(lock)*3) for _ in range (len(lock)*3)]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]


                match(arr, key, rot, row, col)        # key 자물쇠에 매칭하기
                if check(arr, offset, len(lock)):     # 매칭하고 자물쇠 영역 1인지 확인
                    return True

    return False