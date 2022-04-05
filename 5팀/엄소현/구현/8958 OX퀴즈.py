import sys
input = sys.stdin.readline

n = int(input())   # 테스트 케이스 개수
test_case = [input().rstrip() for _ in range(n)]   # 테스트 케이스
result = []   # 각 테스트 케이스 점수

for i in range(n):
    score = 0   # 점수
    now = 0   # 연속된 O의 개수
    for j in test_case[i]:
        if j == 'O':
            now += 1
            score += now
        else:
            now = 0
    result.append(score)

for i in range(n):
    print(result[i])
