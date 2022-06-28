import sys
N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))


for i in range(N-1,0,-1):
  max_num = max(arr[:i+1])
  max_num_idx = arr.index(max_num)
  if max_num_idx != i:
    arr[max_num_idx], arr[i] = arr[i], arr[max_num_idx]
    K -= 1
    if K == 0:
      for i in arr:
        print(i, end=' ')
      sys.exit(0)
  else:
    continue
print(-1)
