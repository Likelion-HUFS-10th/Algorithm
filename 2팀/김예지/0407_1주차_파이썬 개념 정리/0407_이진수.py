T = int(input())

for i in range(T):
    n = int(input())

    for i in range(len(bin(n)[::-1])-2):
        if bin(n)[::-1][i]=='1':
            print(i, end=" ")