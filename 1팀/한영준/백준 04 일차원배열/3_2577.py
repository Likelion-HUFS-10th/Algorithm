# a = int(input())
# b = int(input())
# c = int(input())

# abc = a * b * c
# str_abc = str(abc)

# zero, one, two, three, four, five, six, seven, eight,nine = 0,0,0,0,0,0,0,0,0,0

# for num in str_abc :
#     if num == "0":
#         zero += 1
#     elif num == "1":
#         one += 1
#     elif num == "2":
#         two += 1
#     elif num == "3":
#         three += 1
#     elif num == "4":
#         four += 1
#     elif num == "5":
#         five += 1
#     elif num == "6":
#         six += 1
#     elif num == "7":
#         seven += 1
#     elif num == "8":
#         eight += 1
#     elif num == "9":
#         nine += 1

# print(zero)
# print(one)
# print(two)
# print(three)
# print(four)
# print(five)
# print(six)
# print(seven)
# print(eight)
# print(nine)

a = int(input())
b = int(input())
c = int(input())

abc = a * b * c
str_abc = str(abc)
nums = [0,0,0,0,0,0,0,0,0,0]
     
for num in str_abc :
    if num == "0":
        nums[0] += 1
    elif num == "1":
        nums[1] += 1
    elif num == "2":
        nums[2] += 1
    elif num == "3":
        nums[3] += 1
    elif num == "4":
        nums[4] += 1
    elif num == "5":
        nums[5] += 1
    elif num == "6":
        nums[6] += 1
    elif num == "7":
        nums[7] += 1
    elif num == "8":
        nums[8] += 1
    elif num == "9":
        nums[9] += 1

for i in range(10):
    print(nums[i])

