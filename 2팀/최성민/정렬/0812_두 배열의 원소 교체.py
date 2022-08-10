n, k = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB.sort(reverse=True)

for idx in range(k):
	if listA[idx] < listB[idx]:
		listA[idx], listB[idx] = listB[idx], listA[idx]
	
	else:
		break

print(sum(listA))