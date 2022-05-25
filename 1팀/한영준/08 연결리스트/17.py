import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n")
lst1 = list(line.split("->"))
lst2 = lst1

for i in range(0,len(lst1)-1,2):
    lst1[i] = lst2[i+1]
    lst1[i+1] = lst2[i]
   
print(lst1)

