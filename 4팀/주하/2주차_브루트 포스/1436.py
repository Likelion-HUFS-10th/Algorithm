n = int(input())
cnt = 0
movie = 666 

while True:
    if "666" in str(movie):   # 666부터 입력받은 n까지
        cnt += 1
    if cnt == n:
        print(movie)
        break
    movie = movie + 1
    