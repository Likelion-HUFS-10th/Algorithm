arr = [int(input()) for _ in range(9)]
arr.sort()
s = sum(arr) - 100

def solution():
    for i in range(9):
        for j in range(i+1, 9):
            if arr[i] + arr[j] == s:
                del arr[i]
                del arr[j-1]
                return

solution()  
for i in arr:
    print(i)