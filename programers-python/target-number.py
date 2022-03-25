from collections import deque
num = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    answer = 0
    numberarr = deque(numbers)
    def dfs(arr, start, index):
        if len(arr) == index:
            if start == target:
               nonlocal answer
               answer += 1
            return
        dfs(arr, start + arr[index], index + 1)
        dfs(arr, start - arr[index], index + 1)
        return
    dfs(numberarr, 0, 0)
    return print(answer)

solution(num,target)