"""
빼기를 기준으로 분류하기 더 큰 값 만들어서 빼기
"""
arr = input().split('-')
for i in range(len(arr)):
    if '+' in arr[i]:
        arr[i] = arr[i].split('+')

for i in range(len(arr)):
    if type(arr[i])==list:
        for j in range(1,len(arr[i])):
            arr[i][j] = int(arr[i][j-1])+int(arr[i][j])
        arr[i] = arr[i][-1]

for i in range(1,len(arr)):
    arr[i] = int(arr[i-1]) - int(arr[i])

print(arr[-1])

# if not '-' in arr:
#     arr = arr.split('+')
#     for i in range(len(arr)-1):
#         arr[i] = int(arr[i])+int(arr[i+1])

# else:
#     arr = arr.split('-')
#     for i in range(len(arr)):
#         if '+' in arr[i]:
#             idx = arr[i].find('+')
#             arr[i] =  int(arr[i][:idx]) + int(arr[i][idx+1:])

#     for i in range(len(arr)-1):
#         arr[i] = int(arr[i])-int(arr[i+1])

# print(arr[-2])