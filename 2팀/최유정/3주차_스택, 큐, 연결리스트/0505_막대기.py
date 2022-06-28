import sys
input = sys.stdin.readline


def find_block(list):
    max_num = list[len(list)-1]
    look = 1

    for i in range(len(list), 0, -1):
        if list[i-1] > max_num:
            max_num = list[i-1]
            look += 1
    return(look)

    
n = int(input())
h_list = []
for _ in range(n):
    h_list.append(int(input()))

print(find_block(h_list))