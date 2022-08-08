# import sys

# jangboo = []
# hap = 0

# orders = map(int,sys.stdin.readline())

# for i in (orders) :
#     num = map(int,sys.stdin.readline())

#     if num != 0:
#         jangboo.append(num)
#     else :
#         jangboo.pop()

# for j in jangboo :
#     hap += j

# print(hap)

jangboo = []
hap = 0

orders = int(input())

for i in range(orders) :
    num = int(input())

    if num != 0:
        jangboo.append(num)
    else :
        jangboo.pop()

for j in jangboo :
    hap += j

print(hap)
