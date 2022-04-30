import sys

s = sys.stdin.readline()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
index = 0

for i in range(len(alpha)):
    if alpha[i] in s:
        print (s[alpha[i]])

