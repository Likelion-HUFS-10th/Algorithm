import sys
input = sys.stdin.readline

n, k = map(int, input().split())   # n: 인원 수, k: K번째 사람 제거
people = list(range(n))

num = k - 1   # 제거할 사람 인덱스
pmt = []   # 제거된 사람들
while True:
    pmt.append(str(people.pop(num) + 1))
    if len(people) == 0:
        break
    n -= 1
    num += k - 1
    if num >= n:
        while num >= n:
            num = num - n

print("<"+', '.join(pmt)+">")
