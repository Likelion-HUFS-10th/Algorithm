# 1966 프린터 큐
T = int(input())
for i in range(T):
  N, M = map(int, input().split())
  importance = list(map(int, input().split()))
  for i in range(len(importance)):
    if importance.index(importance[i]) == M:
      importance[M] = [importance[M], "key"]
    else:
      importance[i] = [importance[i], "none"]

  find_num = importance[M]
  cnt = [0]

  def checking(importance, cnt):
    for i in range(len(importance)):
      check = all(importance[0][0] >= importance[i+1][0] for i in range(len(importance)-1))
    if not check:
      importance.append(importance[0])
      importance.pop(0)
    else:
      importance.pop(0)
      cnt.append(cnt[0]+1)
      cnt.pop(0)
      
  while find_num in importance:
    checking(importance, cnt)

  print(cnt[0])