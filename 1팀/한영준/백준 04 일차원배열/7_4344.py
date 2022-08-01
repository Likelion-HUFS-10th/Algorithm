n = int(input())

for _ in range(n):
    jumsoo = list(map(int, input().split()))
    del jumsoo[0]
    cnt = 0
    hap = 0
    for i in range(len(jumsoo)):
        hap = hap + jumsoo[i]
    for score in jumsoo:
        if score > hap/len(jumsoo) :
            cnt += 1
    print(hap/len(jumsoo))
    print(cnt)
    print(f"{cnt/len(jumsoo)*100:.3f}"+"%")
    #, 쓰면 공백 출력, + 쓰면 공백 x

