"""
정렬하기 위해서는 자신보다 큰 숫자가 등장한 순간에 들어가면 된다. 
"""

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

new_arr = [arr[0]]

for i in range(1,n):
    flag=True
    for j in range(len(new_arr)):
        if new_arr[j] > arr[i]:
            new_arr.insert(j,arr[i])
            flag=False
            break
    if flag==True:
        new_arr.append(arr[i])

for num in new_arr:
    print(num)