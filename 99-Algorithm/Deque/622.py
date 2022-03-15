class MyCircualQueue:
    #MyCircualQueue 시작시 초기화 부분
    def __init__(self, k: int):
        #queue선언 -> 큐의 길이를 외부 입력값 k만큼 빈 배열을 생성한다
        self.queue = [None] * k
        #max length 큐 배열의 최대 길이
        self.maxlength = k
        #포인터 해당 변수의 앞인지 뒤인지 판단하는 인덱스
        self.front = 0
        self.rear = 0

    # enQueue(): rear 포인터이동
    # 데이터 삽입 부분 외부의 value값을 받아서 bool타입으로 반환한다. (leetcode 제한사항)
    def enQueue(self, value: int) -> bool:
        #만약 이 배열[rear인덱스]가 가르키는 곳에 데이터가 없으면 이 배열[rear인덱스]에 값을 넣고,
        if self.queue[self.rear] is None:
            self.queue[self.rear] = value
            #rear 포인터에 +1(한칸 옆으로 이동) % 최대길이로 나눠 나머지 값을 넣는다.
            #이렇게 하는 이유는 circle Queue에서 배열을 재사용하기 위함이다.
            self.rear = (self.rear + 1) % self.maxlength
            return True
        else:
            #만일 해당 인덱스에 데이터가 들어있으면 False로 반환한다.
            return False
    # deQueue(): front 포인터 이동
    # 데이터를 빼낼때에는 그곳에 데이터가 있는지 먼저 조회를 한다. 만일 데이터가 없으면 false를 반환한다.
    def deQueue(self) -> bool:
        if self.queue[self.front] is None:
            return False
        #그게 아니라면 해당 지점의 데이터를 삭제한뒤, 프론트를 한칸 옆으로 이동시킨다. (rear 인덱스와 동일하게 최대값으로 나눈 나머지 값을 인덱스로 넣는다.)
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxlength
            return True
    def Front(self) -> int:
        #현재 프론트 인덱스에 데이터가 있으면 해당 인덱스를 반환하고, 만일 인덱스에 데이터가 없으면 -1을 반환한다.
        return -1 if self.queue[self.front] is None else self.queue[self.front]
    def Rear(self) -> int:
        #해당 인덱스는 데이터 마지막의 다음 인덱스를 가리키고 있으므로 -1해서 이전 인덱스를 반환하는데, 그곳에 데이터가 없으면 -1반환하고 데이터가 있으면 해당 인덱스를 반환한다.
        return -1 if self.queue[self.rear - 1] is None else self.queue[self.rear - 1]
    def isEmpty(self) -> bool:
        #배열이 비었는지 확인할려면 front인덱스와rear인덱스가 같은 위치에 있고 배열[front]의 값이 none인경우 이 배열은 빈배열이다.
        return self.front == self.rear and self.queue[self.front] is None
    def isFull(self) -> bool:
        #배열이 꽉차있는지 확인할려면 front인덱스와 rear인덱스가 같은 위치에 있고 배열[front]의 값이 있는 경우 이 배열은 꽉찬 배열이다.
        return self.front == self.rear and self.queue[self.front] is not None

