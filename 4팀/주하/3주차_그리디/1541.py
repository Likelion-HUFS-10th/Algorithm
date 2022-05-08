n = input().split('-')  # -로 분리

# -로 분리되지 않은 값들 합하기
plus_num = 0                  
for _ in range(len(n)):
    if '+' in n[0]:
        first_n = n[0].split('+')
        for i in range(len(first_n)):
            plus_num += int(first_n[i])
    else:
        plus_num = int(n[0])

# - 로 분리된 값들끼리 더하기
minus_num = 0
for l in range(1,len(n)):
    rest_num = n[l].split('+')
    for m in range(len(rest_num)):
        minus_num += int(rest_num[m])

# 최종값 구하기
total = plus_num - minus_num

print(total) 



# n = input().split('-')

# for i in range(len(n)):
#    plus_num = sum(map(int,n[0].split("+")))

# for i in range(1,len(n)):
#    minus_num = sum(map(int,n[i].split("+")))

# total = plus_num - minus_num

# print(total)
