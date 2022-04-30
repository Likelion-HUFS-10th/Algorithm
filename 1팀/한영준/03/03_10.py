import sys
star = int(sys.stdin.readline())

for i in range(star-1, -1, -1):
    print (" "*i + "*"*(star-i))