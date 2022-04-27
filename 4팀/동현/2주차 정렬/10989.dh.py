"""
Bubble sort 알고리즘을 사용
숫자의 크기를 비교해 리스트 내부에서 순서를 바꾸는 방식 사용
런타임 에러 발생..
"""
num_num = int(input('N을 입력하시오: '))
num_list = list(map(int, input().split()))

for i in range(num_num):
    for j in range(1,num_num):
        if num_list[j-1] > num_list[j]:
            num_list[j-1], num_list[j] = num_list[j], num_list[j-1]

for k in range(len(num_list)):
    print(num_list[k])
