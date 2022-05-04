class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def get_index(self, index):
		cnt = 0
		node = self.head
		while cnt < index:
			cnt += 1
			node = node.next
		return node
		
	def append(self, data):
		if self.head == None:
			self.head = Node(data)

		else:
			node = self.head
			while node.next is not None:
				node = node.next
			node.next = Node(data)

	def print(self):
		node = self.head
	
		while node:
			print(node.data, end=" ")
			node = node.next
	
	def listing(self, index, cnt):
		if index-cnt-1 < 0:
			node = self.get_index(index-1)
			target = node.next

			node.next = target.next
			target.next = self.head
			self.head = target
		else:	
			node = self.get_index(index-1)
			change = self.get_index(index-cnt-1)

			target = node.next
			node.next = node.next.next
			target.next = change.next
			change.next = target
		
n = int(input())
pick = list(map(int, input().split()))

ll = LinkedList()

for i in range(1, n+1):
	ll.append(i)

for i in range(1, len(pick)):
	ll.listing(i, pick[i])

ll.print()

