a, b, c = map(int,input().split())
prize = 0
bigger = 0
if (a==b==c):
    prize = 10000 + a*1000

elif (a==b !=c):
    prize = 1000 + a*100

elif (a==c !=b):
    prize = 1000 + a*100

elif (b==c != a):
    prize = 1000 + b*100

else :
    if (a>b):
        if (a>c) :
            bigger = a
        else :
            bigger = c
    else :
        if (b>c) :
            bigger = b
        else :
            bigger = c

    prize = bigger * 100

print (prize)
