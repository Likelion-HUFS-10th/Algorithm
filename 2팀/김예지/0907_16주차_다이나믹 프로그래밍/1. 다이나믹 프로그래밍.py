# # 탑다운 메모이제이션 기법을 통한 피보나치 수열 구현 (함수 이용)

# d = [0] * 100
# # 메모이제이션을 위한 공간을 리스트로 할당

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     elif d[x] != 0:
#         return d[x]
#     else:
#         d[x] = fibo(x - 1) + fibo(x - 2)
#         return d[x]

# print(fibo(99))

# 바텀업 메모이제이션 기법을 통한 피보나치 수열 구현 (반복문)
d = [0] * 100
# DP 테이블 초기화
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])