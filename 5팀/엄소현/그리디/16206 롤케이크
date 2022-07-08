import sys
input = sys.stdin.readline

n, m = map(int, input().split())   # n: 롤케이크 개수, m: 자를 수 있는 최대 횟수
length = list(map(int, input().split()))   # 롤케이크 길이
l1 = []   # 10의 배수 리스트
l2 = []   # 10의 배수가 아닌 리스트
for l in length:
  if l < 10:
    continue
  elif l % 10 == 0:
    l1.append(l)
  else:
    l2.append(l)
l1.sort()
l2.sort()
length = l1 + l2

cut = 0   # 자른 횟수
cnt = 0   # 롤케이크 개수 최댓값

for l in length:
  while True:
    if l < 10:
      break
    elif l == 10:
      cnt += 1
      l -= 10
    else:
      l -= 10
      cnt += 1
      cut += 1
      if cut == m:
        if l == 10:
          cnt += 1
        print(cnt)
        exit(0)
  
print(cnt)
