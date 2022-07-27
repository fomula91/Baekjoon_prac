from collections import deque
price = [1, 2, 3, 2, 3, 1]
def solution(prices):
    answer = []
    jusic = deque(prices)
    while jusic:
        temp = []
        temp.append(jusic.popleft())
        sec = 0
        print(temp, jusic)
        for i in range(len(jusic)):
            if temp[0] <= jusic[i]:
                sec += 1
            elif temp[0] > jusic[i]:
                if sec <= 0:
                    sec = 1
                    break
                else: sec += 1

        answer.append(sec)


    return print(answer)

solution(price)