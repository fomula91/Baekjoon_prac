#가정... 해시 테이블은 제산법을 이용해 해싱을 구현
from collections import defaultdict
class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = None
        
class HashTable:
    def __init__(self):
        self.size = 10000
        self.table = defaultdict(Node)

    def put(self, key, value):
        index = key % self.size
        if not self.table[index].value:
            self.table[index] = Node(key, value)
            return
        node = self.table[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        node.next = Node(key, value)

    def get(self, key):
        index = key % self.size
        if not self.table[index].value:
            return -1
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key):
        index = key % self.size
        if not self.table[index].value:
            return -1
        node = self.table[index]
        if node.key == key:
            if node.next:
                self.table[index] = node.next
                return
            else:
                self.table[index] = None
                return
        prevNode = node
        while node:
            if node.key == key:
                prevNode.next = node.next
                return
            prevNode = node
            node = node.next