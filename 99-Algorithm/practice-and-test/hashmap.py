from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = [0] * bridge_length
    temp = []
    #print(stack, truck_weights)
    while True:
        print('----------start-------------')
        print(f'stack= {stack}{sum(stack)}\ntruck= {truck_weights}{sum(truck_weights)}')
        
        if sum(stack) > 0:
            stack.pop(0)
            answer += 1
            stack.append(0)
            
        if stack[0] <= 0 and len(truck_weights) > 0:
            stack.append(truck_weights.pop(0))
            stack.pop(0)
            answer += 1
        
        elif len(truck_weights) > 0 and sum(stack) <= weight:
            stack.append(truck_weights.pop(0))
            stack.pop(0)
            answer += 1
        elif sum(stack) > 0 and len(truck_weights) <= 0:
            stack.pop(0)
            answer += 1
        else:
            break

        print('----------end----------------')
        
        
    print(answer)
    return answer
    

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

solution(bridge_length,weight,truck_weights)