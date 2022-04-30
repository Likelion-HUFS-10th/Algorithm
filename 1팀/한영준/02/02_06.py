a,b = map(int,input().split())
c = int(input())

if(b+c < 60):
    b = b+c

else :
    a = ((b+c) // 60) + a
    b = (b + c) % 60
    if (a>23):
        a = a-24

print(a, b)