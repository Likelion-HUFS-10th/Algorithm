import sys

line = sys.stdin.readline()
line = line.upper()
pelin = ""

for i in line:
    
    if 64>ord(i) or ord(i)>90 :
        line = line.replace("%s" %i, "")

pelin = line[::-1]

if line == pelin :
    print("True")

else:
    print("False")