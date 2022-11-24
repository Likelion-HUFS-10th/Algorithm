n,k = map(int,input().split())

table = list(input())

result = 0

for i,j in enumerate(table):
    if j == 'P':
        flag = False
        for a in range(max(0, i-k),min(n,i+k+1)):
            if flag == False and table[a] == 'H':
                table[a] = 'h'
                result += 1
                flag = True
                
print(result)