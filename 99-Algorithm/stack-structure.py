class Node:
    #노드 클래스 구현, 스택에 필요한 밸류와 이전값을 지정합니다.
    def __init__(self, value, next):
        self.value = value
        self.next = None

class Stack:
    #스택클래스를 구현
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None

    #데이터를 집어 넣을때, 값과, 노드의 다음값을 지정합니다.
    def push(self, value):
        self.top = Node(value, next)

    #데이터를 꺼낼때, 만약 스택이 빈 배열이면 none을 리턴하고 그렇지 않으면
    #현재의 top데이터를 임시 변수에 저장하고, 현재의 top데이터를 노드의 다음 값으로 지정
    #임시 변수node에 저장된 데이터를 리턴합니다.
    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next

        return node.value
        