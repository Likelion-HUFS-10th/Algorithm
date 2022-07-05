num = int(input())
num_list = list(map(int, str(num)))
result = num_list[0]

for i in range(len(num_list)-1):
    if num_list[i] == 0 or num_list[i] == 1:
        result += num_list[i+1]
    else:
        result *= num_list[i+1]

print(result)