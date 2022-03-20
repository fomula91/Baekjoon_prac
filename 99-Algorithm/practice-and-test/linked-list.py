class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        return

    def __str__(self) -> str:
        return f"Node {{ value: {self.value}, next: {self.next} }}"

class LinkedList:
    head: Node
    def __init__(self):
        self.head = None

    # 추가
    def append(self, value):
        if not self.head:
            self.head = Node(value, None)
            return
        
        node = self.head
        while node:
            if not node.next:
                node.next = Node(value, None)
                break
            node = node.next

    # 삽입
    def insert(self, index ,value):
        if not self.head:
            self.head = Node(value, None)
            return
        if index == 0:
            node = Node(value, self.head)
            self.head = node
            return

        prevNode = self.head
        node = self.head.next
        nodeIndex = 1
        while node:
            if nodeIndex == index:
                node = Node(value, node)
                prevNode.next = node
                return

            prevNode = node
            node = node.next
            nodeIndex += 1
        prevNode.next = Node(value, None)

    # 맨뒤 데이터 삭제
    def pop(self):
        if not self.head:
            return None
            
        node = self.head
        while node.next:
            prevNode = node
            node = node.next
        prevNode.next = None
        return node.value

    # 중간 데이터 삭제
    def remove(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return

        prevNode = self.head
        node = self.head.next
        nodeIndex = 1
        while node:
            if nodeIndex == index:
                prevNode.next = node.next
                return
            prevNode = node
            node = node.next
            nodeIndex += 1

    # 데이터 얻기
    def get(self, index):
        if not self.head:
            return None

        node = self.head
        nodeIndex = 0
        while node:
            if nodeIndex == index:
                return node.value
            node = node.next
            nodeIndex += 1
        return None
        

    # 데이터 위치 얻기
    def index(self, value):
        if not self.head:
            return
        node = self.head
        index = 0
        while node:
            if node.value == value:
                return index
            index += 1

lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
#lst.remove(2)
lst.get(0)
#print(lst.head)
#print(lst.head.next)

    # def append(self, value):
    #     if not self.head:
    #         self.head = Node(value, None)
    #         return
        
    #     node = self.head
    #     while node.next:
    #         node = node.next
    #     node.next = Node(value, None)

    # def pop(self, value):
    #     if not self.head:
    #         return None
        
    #     node = self.head
    #     while node:
    #         if node.value == value:
    #             node = node.next