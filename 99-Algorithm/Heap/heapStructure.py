#힙을 사용하는 이유 -> 데이터에서 최대, 최소값을 찾아야할때 빠르게 그 값을 찾기 위해 고안된 완전 이진트리이다.
#힙은 max heap, min heap이 있다.


class BinaryMaxHeap:
    #클래스를 시작할때 가장 먼저 생성된다.
    def __init__(self):
        self.item = [None]
    #함수를 오버라이딩 한다. __'함수 이름'__은 매직매서드이다.
    #https://wikidocs.net/83755
    #자세히 공부해야되는 내용은 블로그에 작성한다.
    def __len__(self):
        #기존 배열에 -1 값을 더한 결과를 리턴한다. 기존 배열에 None항목이 기본적으로 생성하였기 때문
        return len(self.item) - 1
    #precolate스며들다 현재 함수에서 부모와 자식 노드를 검사해서 만일 자식노드가 부모노드보다 큰 경우 부모노드와 자식 노드를 서로 위치를 바꿔준다.
    def _percolate_up(self):
        #현재 노드는 배열의 길이
        cur = len(self)
        #부모 노드는 현재 노드의 절반 값
        parent = cur // 2
        #만일 부모의 노드가 0보다 크면 반복한다.
        #parent 값이 0이거나 0보다 작은 경우 False를 반환하기 때문이다.
        while parent > 0:
            #반복중에 현재 노드의 값이 부모 노드의 값보다 크면
            if self.item[cur] > self.item[parent]:
                #현재 노드와 부모 노드의 위치를 서로 교환한다.
                self.item[cur], self.item[parent] = self.item[parent], self.item[cur]
            #현재 노드변수에 부모 노드 변수를 넣는다.
            cur = parent
            parent = cur // 2
            #최종적으로 parent가 0이되면 반복을 종료한다.
    
    #힙 배열에서 원소를 추출할때 가장 큰 값을 추출한다.
    def _percolate_down(self, cur):
        #현재 노드를 가장 큰값 변수에 넣는다.
        biggest = cur
        #현재 노드x2하면 왼쪽 노드가 된다.
        left = 2 * cur
        #현재 노드x2하면 오른쪽 노드가 된다.
        right = 2 * cur + 1
        #이 과정은 배열상에서 보면 [None,'3'첫번째인덱스 ,6:왼쪽노드,7:오른쪽노드,2,5,4]
        #인덱스로 보면 2x1(현재인덱스) = 2 => 2.value = 6
        #          2x1 + 1 = 3 => 3.value = 7

        #왼쪽 인덱스가 배열의 길이보다 작거나 같고, 배열의 [left]요소가 배열의[biggest]요소보다 클경우
        if left <= len(self) and self.item[left] > self.item[biggest]:
            #인덱스를 서로 바꿈
            biggest = left
        #오른쪽 인덱스가 배열의 길이보다 작거나 같고, 배열의[right]요소가 배열의[bigest]요소보다 클경우
        if right <= len(self) and self.item[right] > self.item[biggest]:
            #인덱스를 서로 바꿈
            biggest = right
        #만일 biggest 인덱스가 cur인덱스와 값이 다르다면
        if biggest != cur:
            #배열의[cur]요소와 배열의[biggest]요사를 서로 바꾼다
            self.item[cur], self.item[biggest] = self.item[biggest], self.item[cur]
            #재귀적으로 큰값을 찾아 배열의 요소를 재정렬 한다.
            self._percolate_down(biggest)
        #위 과정이 끝나면 힙의 구성 특징을 유지할수 있다.
        #재귀적으로 리프노드까지 갔을 경우 마지막 왼쪽 오른쪽 값은 현재 배열보다 크고 매개변수는 변화가 없으므로 재귀가 종료된다.
    #배열의 새값을 넣을 경우 _percolate_up함수를 이용해 배열을 재정렬한다.
    #percolate_up함수를 이용하는 이유는 maxheap의 특성을 유지하기 위해서이다.
    def insert(self, k):
        self.item.append(k)
        self._percolate_up()
    #배열에서 아이템을 추출할때,
    def extract(self):
        #만일 배열의 길이가 0이라면 None을 반환한다.
        if len(self) < 1:
            return None
        #root값에 배열의 첫번째 인덱스를 넣는다.
        #배열의 첫번째 인덱스는 max heap구조에서 가장 큰값이므로, 배열에서 가장 큰값을 root변수에 저장한다.
        root = self.item[1]
        #배열의 첫번째 인덱스와 배열의 마지막 인덱스의 요소를 서로 바꾼다.
        self.item[1] = self.item[-1]
        #배열의 마지막 요소를 추출한다.
        self.item.pop()
        #percolate_down 함수를 이용해 배열을 max heap의 특성에 맞게 재정렬한다.
        self._percolate_down(1)
        #맨처음 저장한 배열의 큰값을 반환한다.
        return root

b = BinaryMaxHeap()
b.insert(10)
b.insert(5)
b.insert(8)
b.insert(1)
print(b.item)