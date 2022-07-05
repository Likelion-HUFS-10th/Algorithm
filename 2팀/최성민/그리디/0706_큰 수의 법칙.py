"""
큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 						   더하여 가장 큰 수를 만드는 법칙
              단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수는 없다.
"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

arr.sort()
a = arr.pop()
b = arr.pop()

cntA = m // k
cntB = m % k

ans = a * (k * cntA) + (b * cntB)

print(ans)

"""
arr.sort()
first = arr[n-1]
second = arr[n-2]

count = int(m / (k+1)) * k
count += m % (k + 1)

ans += count * first
ans += (m - count) * second

print(ans)
"""