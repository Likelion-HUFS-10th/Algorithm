"""
배수니까 흔히 알고 있는 그리디를 써도 됨.
"""

n,k = map(int,input().split())
coin_arr = [
    int(input())
    for _ in range(n)
]

coin_arr.sort(reverse=True)
cnt=0
for i in range(n):
    if coin_arr[i]>k:
        continue
    else:
        cnt += k//coin_arr[i]
        k = k%coin_arr[i]

print(cnt)
