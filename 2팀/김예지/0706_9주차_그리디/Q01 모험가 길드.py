N = int(input())
mem_lst = list(map(int, input().split()))
mem_lst.sort()
cnt = 0
waiting = 0

for mem in mem_lst:
  waiting += 1
  if waiting >= mem:
    waiting -= mem
    cnt += 1

print(cnt)
