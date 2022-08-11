N = int(input())
array = []
for _ in range(N):
    array.append(input().split())

def setting(data):
    return data[1]
    
array = sorted(array, key = setting)

for i in array:
    print(i[0], end = " ")