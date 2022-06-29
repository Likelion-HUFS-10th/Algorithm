import math

while True:
    case, n = map(str, input().split())
    case = list(case)
    unpack_case = ''.join(case)
    case.sort()
    n = int(n)
    final_n = n
    printing = []
    cnt = 0

    def factor(num):
        return math.factorial(num)

    if factor(len(case)) < n:
        print(f'{unpack_case} {n} = No permutation')
    else:
        while case:
            cnt = 0
            share_num = factor(len(case)) / len(case)
            idx_num = share_num
            while idx_num < n:
                idx_num += share_num
                cnt += 1
            printing.append(case[cnt])
            case.remove(case[cnt])
            rested = n - (idx_num - share_num)
            n = rested
        unpacking = ''.join(printing)
        print(f'{unpack_case} {final_n} = {unpacking}')

# runtimeerror