arr = input().rstrip().split('-')

for i in range(len(arr)):
    if '+' in arr[i]:
        arr[i] = arr[i].split('+')

for i in range(len(arr)):
    if type(arr[i]) == list:
        for j in range(1,len(arr[i])):
            arr[i][j] = int(arr[i][j-1])+int(arr[i][j])
        arr[i] = arr[i][-1]

result = int(arr[0])

for i in range(1,len(arr)):
    result-=arr[i]

print(result)