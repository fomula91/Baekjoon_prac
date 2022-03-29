#https://programmers.co.kr/learn/courses/30/lessons/42889
# from itertools import count 
N = 5
stages = [3, 1, 2, 2, 2]
# result = [3,4,2,1,5]
def solution(N, stages):
    answer = []
    people = []
    temp = []
    peopleCount = len(stages)

    for i in range(1, N+1):
        people.append(stages.count(i))

    for i in range(N):
        if people[i] == 0:
            temp.append((i+1,0))
            continue
        temp.append((i+1,(people[i]/peopleCount)))
        peopleCount = peopleCount - people[i]

    temp.sort(key=lambda x: -x[1])
    for i in temp:
        answer.append(i[0])
    print(f'내풀이 {answer}')















def solutions(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    print(f'정답 {answer}')
solution(N, stages)
solutions(N, stages)