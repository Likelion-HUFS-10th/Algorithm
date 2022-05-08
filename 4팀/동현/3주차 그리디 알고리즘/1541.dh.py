"""
숫자가 0009와 같은 형태일 경우 처리
int()를 통한 형변환을 할 경우 0009 > 9로 적용되기 때문에 0을 제거하는 과정이 필요가 없음
"""
# 방법 1: 0을 모두 제거해주는 방법
ex = input()
num_list = ex.split('+')
num_list = [num.lstrip('0') if len(num) > 0 and num.startswith('0') else num for num in num_list]
ex1 = '+'.join(num_list)

num_list1 = ex1.split('-')
num_list1 = [num.lstrip('0') if len(num) > 0 and num.startswith('0') else num for num in num_list1]
ex2 = '-'.join(num_list1)

num_list2 = ex2.split('-')
result_list = []

for i in num_list2:
    if '+' in i:
        plus = 0
        plus_list = i.split('+')
        for j in plus_list:
            plus += int(j)
        result_list.append(plus)
    else:
        result_list.append(i)

num_first = int(result_list[0])
for j in range(1,len(result_list)):
    num_first -= int(result_list[j])
print(num_first)


# 방법 2: 형 변환을 통한 방법
ex = input()
num_list2 = ex.split('-')
result_list = []

for i in num_list2:
    if '+' in i:
        plus = 0
        plus_list = i.split('+')
        for j in plus_list:
            plus += int(j)
        result_list.append(plus)
    else:
        result_list.append(i)

num_first = int(result_list[0])
for j in range(1,len(result_list)):
    num_first -= int(result_list[j])
print(num_first)