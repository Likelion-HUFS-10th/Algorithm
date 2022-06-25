T = int(input())
n = list(map(int, input().split()))
for i in range(T):
    bin_num = bin(n[i])
    bin_num_list = list(map(int, str(bin_num)[:1:-1]))
    num_one = []
    for j in range(len(bin_num_list)):
        if bin_num_list[j] == 1:
            num_one.append(j)
    print(num_one)