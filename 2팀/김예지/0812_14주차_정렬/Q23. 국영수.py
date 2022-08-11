N = int(input())
array = []
for _ in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

array = sorted(array, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in array:
    print(student[0])

# Insertion Sort
# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j-1][1] < array[j][1]:
#             array[j-1], array[j] = array[j], array[j-1]
#         elif array[j-1][1] == array[j][1]:
#             if array[j-1][2] > array[j][2]:
#                 array[j-1], array[j] = array[j], array[j-1]
#             elif array[j-1][2] == array[j][2]:
#                 if array[j-1][3] < array[j][3]:
#                     array[j-1], array[j] = array[j], array[j-1]
#                 elif array[j-1][3] == array[j][3]:
#                     if ord(array[j-1][0][0]) > ord(array[j][0][0]):
#                         array[j-1], array[j] = array[j], array[j-1]

# for student in array:
#     print(student[0])