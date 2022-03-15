#배열과 링크드리스트
# 배열 -> 자리가 고정되있다. O(1)의 시간복잡도 // 자리가 고정되있어 수정/삭제가 어렵다
#
# 링크드리스트 -> 연결된 리스트 O(n)의 시간복잡도 자리가 고정되있지 않아 수정/ 삭제가 쉽다
#                      array               linked-list
#특정원소 조회          O(1)                    O(n)
#중간에 데이터 삽입      O(n)                    O(1)
#데이터 추가           데이터 추가시 모든 공간이      모든 공간이 다 찼어도 맨뒤의 노드만
#                   다 차버린다면 새로운 메모리     동적으로 추가하면된다
#                   공간을 할당받아야된다
#정리                데이터 접근이 빈번하다면       삭제, 삽입이 빈번하다면
#                   array를 이용하자           linkedlist를 사용하는 것이 좋다
#
#클래스의 구현
class Person:
    #__init__ 매직메서드, 반드시 먼저 실행된다.
    def __init__(self, name):
        #self의 이름으로 지정한다. -> self는 해당 함수를 지칭한다.
        self.name = name
    def sayhello(self, to):
        print(f"hello {to}, i'm {self.name}")

rtan = Person('rtanny')
rtan.sayhello("hanghea")

#연결리스트가 필요한것 노드와 포인터
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkList:
    #삽입, 삭제가 필요
    def __init__(self):
        self.head = None
        pass
    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)
    

lst = [1,2,3]
l1 = LinkList()
for e in lst:
    l1.append(e)
print(l1)
        