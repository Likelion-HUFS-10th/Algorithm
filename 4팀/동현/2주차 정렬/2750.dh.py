"""
bubble sort가 런타임 에러가 발생하길래
새로운 방법으로 접근했습니다.
"""
num_num = int(input())
num_list =[]

for j in range(num_num):
    num = int(input())
    num_list.append(num)

new_list = sorted(set(num_list))

for i in range(len(new_list)):
    print(new_list[i])