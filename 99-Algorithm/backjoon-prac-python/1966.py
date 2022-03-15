#collections.deque()를 임포트 합니다.
from collections import deque
#https://url.kr/nbjvf6
#max(), min() 함수에 관한 내용

#test케이스 입력
testCase = int(input())

#테스트 케이스만큼 반복문을 돌림
for _ in range(testCase):
    #두번째 입력을 받습니다. 두번째는 docNum은 출력할 문서의 queue, targetIdx는 찾고자하는 문서의 인덱스입니다
    docNum, targetIdx = map(int, input().split())
    #queue변수에 해당 문서의 중요도를 넣습니다. (index 0부터 ducNum까지)
    queue = deque(map(int, input().split()))
    #docNum을 list형태로 변환합니다.
    docQueue = deque(map(int, range(docNum)))
    #targetIdx가 몇번째에 나오는지 확인하는 변수입니다.
    count = 1
    #queue의 길이만큼 반복해서 queue의 요소가 문제에서 찾는 인덱스인지 검사합니다.
    #queue가 빈 배열로 바뀔때 자동으로 while문을 빠져나오게 됩니다.
    while queue:
        #만일 queue[0]이 queue내 최고 중요도일경우 pop을 해서 리스트에서 제외합니다.
        if queue[0] == max(queue):
            queue.popleft()
            #같이 돌고 있던 docQueue도 해당 targetIdx가 아닐경우 빠지게 됩니다.
            #만일 docQueue가 찾고자 하는 인덱스일경우 print를 반환합니다.
            if docQueue.popleft() == targetIdx:
                print(count)
            #위의 경우가 아니라면 count에 1을 더해 반복문을 반복합니다.
            count += 1
        else:
            #만일 queue[0]가 queue내에 최고 중요도가 아닐경우 리스트의 첫번째 값을 리스트에서 맨뒤로 보냅니다.
            queue.append(queue.popleft())
            docQueue.append(docQueue.popleft())