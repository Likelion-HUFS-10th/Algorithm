from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())   # 테스트 케이스 개수
result = []   # 결과 저장

for i in range(test_case):
    n, p_num = list(map(int, input().split()))   # 문서 개수, 몇 번째로 인쇄되었는지 궁금한 문서가 몇 번째에 놓여 있는지
    imp = deque(list(map(int, input().split())))   # n개 문서의 중요도
    inx = deque(list(range(len(imp))))   # 문서 인덱스

    order = 0   # 순서

    while imp:
        if imp[0] == max(imp):
            order += 1
            if inx[0] == p_num:
                result.append(order)
                break
            imp.popleft()
            inx.popleft()
            
        else:
            imp.append(imp.popleft())
            inx.append(inx.popleft())

for i in range(test_case):
    print(result[i])
