from collections import defaultdict
class MyHash:
    #초기화
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    #삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        #인덱스가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        #개별 체이닝 방식으로 구현한 해시 테이블 삽입방법 구현
        p = self.table[index]
        while p:
            #p.key는 해시 테이블 안에서의key값이고, key값은 외부에서 입력받은 인덱스 값이다
            #따라서 p.key와 key의 값이 같다는건 같은 인덱스를 가리킨다는 의미고
            #p.key와 key의 값이 다르다는건 다른 인덱스를 가리킨다는 의미로
            #만일 이 값이 다를 경우 p.next에 새로운 노드를 생성에 데이터를 넣는다.
            if p.key == key:
                p.value = value
                return print('hash table update!')
            if p.next is None:
                break
            #만일 p의 p.next값에 데이터가 들어있다면
            #p.next의 데이터를 p에 넣는다. 그리고 다시 검사한다.
            p = p.next
        p.next = ListNode(key, value)
        print('linked list update!')

    #조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        #노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        #노드가 존재하는 데 일치하는 키 값을 찾지 못한다??
        return -1

    #삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        #인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            #삭제할때 뒤에 노드가 있다면 뒤에 노드를 땡겨오고 그게 아니라면 빈 노드로 변경한다.
            #만일 삭제할때 self.table[index]를 None으로 설정되면 추가/조회 메서드에서 오류가남 왜??
            self.table[index] = ListNode() if p.next is None else p.next
            return

        #연결리스트 노드 삭제
        prev = p
        while p:
            #self.table[index]의 첫번째 노드가 걸리지 않는 이유는 위 코드에서 첫번째 노드를 이미 걸러냈기 때문...
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p.next

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

test = MyHash()