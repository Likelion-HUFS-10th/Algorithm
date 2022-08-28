"""
최빈값 -> 계수정리 방식으로 접근 => 마이너스 값에 대한 처리가 안됨
"""
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

def find_average(array):
    print(sum(array)//n)

def find_mid(array):
    array.sort()
    print(array[int((n-1)/2)])

def find_mode(array):
    num_list = []
    max_num = 0
    for i in array:
        if array.count(i) > max_num:
            max_num = array.count(i)
    
    for j in array:
        if array.count(j) == max_num:
            num_list.append(j)
    result = list(set(num_list))
    result = sorted(result)
    if len(result) >= 2:
        print(result[1])
    else:
        print(result[0])
    
def find_range(array):
    array.sort()
    print(array[-1]-array[0])

find_average(array)
find_mid(array)
find_mode(array)
find_range(array)