n = int(input())
arr = [-1] * 5001
arr[:6] = [-1, -1, -1, 1, -1, 1]

if n > 5:
    for i in range(6, n+1):
        if arr[i-3] != -1 and arr[i-5] != -1:
            arr[i] = min(arr[i-3], arr[i-5]) + 1
        else:
            if arr[i-3] != -1 and arr[i-5] == -1:
                arr[i] = arr[i-3] + 1
            elif arr[i-3] == -1 and arr[i-5] != -1:
                arr[i] = arr[i-5] + 1

print(arr[n])
