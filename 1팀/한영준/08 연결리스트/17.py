import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n")
lst1 = list(line.split("->"))
lst2 = lst1 #원본 보존

for i in range(0,len(lst1)-1,2):
    lst1[i] = lst2[i+1] #원래 인덱스 i+1에 있던걸 i에
    lst1[i+1] = lst2[i] #원래 인덱스 i에 있던걸 i+1에
   
print(lst1)

