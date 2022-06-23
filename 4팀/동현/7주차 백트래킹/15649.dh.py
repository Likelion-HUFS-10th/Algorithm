""""
백트래킹 > 현재 가능한 모든 경로를 탐색
num_list를 회전하며 해주고 싶었지만 특정 M 값에서만 가능
출력 > asterisk 사용
계속 clear()로 해주려고 시도 -> pop()함수 참고
"""
import sys
N, M = map(int, sys.stdin.readline().split())

# num_list = []
# for i in range(N):
#     num_list.append(i+1)

result_list = []

def print_sequence():
    for i in range(1,N+1):
        if i in result_list:
            continue
            
        result_list.append(i)
        print_sequence()
        result_list.pop()

    if len(result_list) == M:
            print(*result_list)
        
print_sequence()