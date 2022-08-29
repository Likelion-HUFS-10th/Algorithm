max_size = 1000000
n = int(input()) #부품의 개수
stock = [0 for _ in range(max_size+1)]

for i in input().split():
    stock[int(i)] = 1

m = int(input()) #요청한 부품의 개수
arr = list(map(int,input().split()))

for i in range(m):
    if stock[arr[i]] == 1:
        print('yes',end=' ')
    else:
        print('no',end=' ')