n = int(input()) #부품의 개수
stock = list(map(int,input().split()))
stock.sort()

m = int(input()) #요청한 부품의 개수
arr = list(map(int,input().split()))

def binary_search(stock, target, start, end):
    if start > end:
        return False

    mid = (start+end)//2

    if stock[mid] > target:
        return binary_search(stock, target, start, mid-1)
    elif stock[mid] == target:
        return True
    else:
        return binary_search(stock, target, mid+1, end)

for i in range(m):
    if binary_search(stock, arr[i], 0, n-1):
        print("yes",end=' ')
    else:
        print("no", end=' ')
