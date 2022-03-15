from collections import deque
#백준 2164문제
#https://www.acmicpc.net/problem/2164
#카드의 갯수를 입력받습니다.
num = int(input())
#deque를 이용해 빈 배열을 생성합니다.
queue = deque()
#카드의 갯수만큼 배열안에 데이터를 집어넣습니다.
for i in range(num):
    queue.append(i+1)
    print(queue)
#배열의 데이터로 카드를 검사합니다.
for _ in range(len(queue)):
    #만일 배열의 길이가 1이라면 그 즉시 반복문을 중단합니다.
    if len(queue) == 1:
        break
    #만일 배열의 길이가 1이상이라면 배열의 첫번째 데이터는 pop으로 버리고 두번째 데이터는 뒤로 보냅니다.
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])