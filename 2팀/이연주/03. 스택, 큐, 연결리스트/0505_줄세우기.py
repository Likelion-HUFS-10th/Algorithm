from dataclasses import dataclass


n = int(input())
students = list(map(int, input().split()))
answer = []

for i in range(n):
    go = students[i]
    answer = answer[:i-go] + [i+1] + answer[i-go:]

print(*answer)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        answer = ""
        next_node = self.head
        while next_node != None:
            answer += str(next_node.data)
            next_node = next_node.next
        return answer

    def swapping(self, node, target):
        next_node = self.head
        while next_node.data == node:
            
