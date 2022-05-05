n,k = map(int,input().split())
coins_list = [ int(input()) for i in range(n)]

cnt = 0 
for i in coins_list[::-1]:       # 큰 동전부터 사용
    cnt += k // i                # cnt에 k를 동전으로 나눈 몫 저장
    k = k % i                    # k에는 동전으로 나눈 나머지 저장
    
print(cnt)
