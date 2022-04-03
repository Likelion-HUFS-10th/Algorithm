n = int(input())
T = [int(input()) for _ in range(n)]

for case in T:
    binary_num = list(bin(case)[2:])
    for i in range(len(binary_num)):
        if binary_num[-i-1] == '1':
            print(i, end=" ")
    print()
