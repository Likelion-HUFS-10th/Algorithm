import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n")
lst = list(line.split("->"))
pellin = ""

for i in range (len(lst)) :
    pellin = lst[i] + " " + pellin

pellin = list(pellin.split())

if lst == pellin:
    print("True")
else :
    print("False")