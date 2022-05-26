import sys #input보다 좀 더 빠른 입력을 위해

line1 = sys.stdin.readline()
line1 = line1.strip("\n")
lst1 = list(line1.split("->"))

line2 = sys.stdin.readline()
line2 = line2.strip("\n")
lst2 = list(line2.split("->"))

lst3 = lst1 + lst2
lst3.sort()

print(lst3)