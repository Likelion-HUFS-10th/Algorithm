import sys

a,b = sys.stdin.readline().split()
re_a = ''
re_b = ''

for i in a:
    re_a = i + re_a

for i in b:
    re_b = i + re_b

if int(re_a) < int(re_b):
    print (re_b)
elif int(re_a) > int(re_b):
    print (re_a)

