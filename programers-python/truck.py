from collections import deque
bridge_len = 100
trucksss = [10,10,10,10,10,10,10,10,10,10]
weight = 100


def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    onBridge = 0
    
    while stack:
    #     print(f'stack is {stack}\nsec is {answer}\ntruck is {trucks}\n')
    #     print(f'onbridge is {onBridge}\n waitTrucks is {waitTrucks}\n\n')
        
        
        onBridge -= stack.popleft()
        answer += 1
        if trucks:
            if onBridge+trucks[0] <= weight:
                truck = trucks.popleft()
                stack.append(truck)
                onBridge += truck
            else:
                stack.append(0)
                
    return print(answer)

solution(bridge_len, weight, trucksss)