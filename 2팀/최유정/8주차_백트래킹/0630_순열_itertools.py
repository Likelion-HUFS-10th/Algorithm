from itertools import permutations
import sys
input = sys.stdin.readline
import math

try:
    while True:
        testcase, num = input().split(' ')
        num = int(num)
        case = list(testcase)
        cnt = 0
        ans = []
        if math.factorial(len(testcase)) < num:
            print(testcase, num, "=", "No permutation")
        else:
            for i in permutations(case):
                cnt += 1
                if cnt == num:
                    print(testcase, num, "=", "".join(i))
except:
    exit()