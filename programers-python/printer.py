priorities = [2, 1, 3, 2]
location = 2

def solution(priorities, location):
    answer = 0
    num = [i for i in range(len(priorities))]

    while True:
        tempPio = priorities[0]
        for i in range(len(num)):
            if tempPio < priorities[i]:
                tempPio = priorities[i]
        
        if tempPio > priorities[0]:
            priorities.append(priorities.pop(0))
            num.append(num.pop(0))
        if tempPio == priorities[0]:
            if location == num[0]:
                answer += 1
                break
            priorities.pop(0)
            num.pop(0)
            answer += 1
    return print(answer)

    

solution(priorities, location)