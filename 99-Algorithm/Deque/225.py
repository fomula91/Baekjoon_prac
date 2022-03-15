import collections
#deque 설명
# https://docs.python.org/ko/3/library/collections.html#collections.deque

class MyStack:
    #클래스 MyStack에서 가장 처음으로 실행된다.
    def __init__(self):
        #queue변수는 collections.deque()를 저장한다.
        #deque는 리스트와 다르가 앞, 뒤로 검색할수 있다.
        self.queue = collections.deque()
    def push(self, x: int) -> None:
        #queue 배열에 x를 삽입한다.
        self.queue.append(x)
        #요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.queue) - 1):
            #새로운 데이터를 삽입하면 기존에 저장되있던 데이터는 popleft에 의해 추출되고 배열에 새롭게 추가된다.
            #이 과정을 배열의 길이 - 1 만큼 반복한다.
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        #현재 배열에서 가장 최상단...(가장 나중에 들어온 데이터)는 배열[0]이므로 deque.popleft()를 사용하여 배열 왼쪽의 데이터를 꺼낸다.
        return self.queue.popleft()
        

    def top(self) -> int:
        #현재 배열에서 가장 마지막에 들어온 데이터는 위 push과정에서 봤듯이 배열[0]번째 이므로 배열[0]을 리턴한다.
        return self.queue[0]
    

    def empty(self) -> bool:
        # 해당 배열이 비었는지 확인할려면 배열으 길이를 보면 비었는지 데이터가 있는지 판별할수 있다.
        return len(self.queue) == 0
