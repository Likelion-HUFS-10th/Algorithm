import sys

line = sys.stdin.readline()
count = line.count(" ") +1

if line[0] == " ":
    count = count-1

if line[len(line)-2] == " ":
    count = count-1

print (count)
