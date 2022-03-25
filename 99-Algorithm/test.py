class BinaryMaxHeap:
    def __init__(self):
        #아이템을 생성해서 빈값을 넣는다.
        self.item = [None]

    def __len__(self):
        #ren함수를 오버라이딩 한다.
        #최종적으로 배열의 현재 길이에서 빈값을 뺀 길이를 반환한다.
        return len(self.item) - 1

    def percolateUp(self):
        #현재 노드 인덱스를 배열의 마지막 인덱스로 넣는다.
        #부모 노드 인덱스를 현재 노드 인덱스의 절반 값을 넣는다.
        #반복문을 부모 노드의 인덱스가 0이 될때까지 반복한다.
            #만일 현재노드인덱스의 값이 부모노드인덱스의 값보다 클경우
            #현재 노드의 인덱스의 요소와 부모노드 인덱스의 요소를 서로 바꾼다.
            #현재 노드인덱스를 부모 노드인덱스로 바꾼다.
            #부모노드인덱스를 현재노드 인덱스의 절반값을 넣는다.
        curNode = len(self)
        parentNode = curNode // 2
        while parentNode > 0:
            if self.item[curNode] > self.item[parentNode]:
                self.item[curNode], self.item[parentNode] = self.item[parentNode], self.item[curNode]
            curNode = parentNode
            parentNode = curNode // 2

    def percolateDown(self, curIndex):
        #현재 함수에서 받은 매개변수는 배열의 가장 큰값 인덱스 이므로
        #최대값변수에 매개변수를 넣는다.
        #왼쪽 변수를 생성해 (2 * 매개변수인덱스)를 넣는다.
        #오른쪽 변수를 생성해 (2 * 매개변수인덱스 + 1)를 넣는다.
        #만일 왼쪽 인덱스보다 최대값인데스가 클경우
        #   왼쪽 인덱스와 최대값인덱스를 서로 바꾼다.
        #만일 오른쪽 인덱스가 최대값인덱스보다 클경우
        #   오른쪽 인덱스와 최대값인덱스를 서로 바꾼다
        #만일 최대값 인덱스와 현재 인덱스가 다를경우
        #   서로의 인덱스의 요소를 바꾼다.
        #   재귀적으로 반복해서 힙을 정렬한다.
        biggest = curIndex
        left = 2 * curIndex
        right = 2 * curIndex + 1
        if left <= len(self) and self.item[left] > self.item[biggest]:
            biggest = left
        if right <= len(self) and self.item[right] > self.item[biggest]:
            biggest = right
        if biggest != curIndex:
            self.item[biggest], self.item[curIndex] = self.item[curIndex], self.item[biggest]
            self.percolateDown(biggest)
        
    def insert(self, inputData):
        #배열에 값을 넣는 작업을 한다.
        #매개변수에들어갈 값을 정하고, 배열에 추가한다.
        #percolate up함수를 이용해 배열을 정렬한다.
        
        self.item.append(inputData)
        self.percolateUp()
        
    def extract(self):
        #맥스힙구조에서 배열의 첫번째 인덱스가 가장 큰값이므로, 가장 큰값을 추출하면 된다.
        #최종적으로 반환할 변수에 첫번째 인덱스를 가진 요소를 넣는다.
        #첫번째 인덱스의 요소와 마지막 인덱스의 요소를 서로 바꾼다.
        #마지막 요소의 인덱스를 뺀다.
        #percolateDown함수에 첫번째 인덱스를 넣고 해당 함수를 이용해 힙을 재정렬한다.
        #맨처음 저장한 변수를 리턴한다.
        root = self.item[1]
        self.item[1] = self.item[-1]
        self.item.pop()
        self.percolateDown(1)
        return root

b = BinaryMaxHeap()
b.insert(1)
b.insert(4)
b.insert(19)
b.insert(29)
b.insert(6)
b.extract()
b.extract()
print(b.item)