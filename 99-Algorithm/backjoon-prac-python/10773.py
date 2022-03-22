# import sys
# input = sys.stdin.readline()
# stack = []
# for i in range(int(input)):
#     callNum = int(sys.stdin.readline().strip())
#     if callNum == 0:
#         stack.pop()
#     else: stack.append(callNum)
# print(sum(stack))
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    result = []
    day = 0
    while progresses:
        day += 1
        progresses = [pro + spd for pro,spd in zip(progresses, speeds)]
        print(progresses)
        for _ in range(len(progresses)):
            if progresses[0] >= 100:
                result.append(progresses.pop(0))
                speeds.pop(0)
        if len(result) != 0:
                print('answer append !!!!')
                answer.append(len(result))
                result = []
        print(f'day is {day}\n')
    return print(answer)

solution(progresses, speeds)
