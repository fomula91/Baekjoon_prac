candidates = [2,3,6,7]
targetNum = 7
def CombinationSum(cardiates, target):
    result = []
    
    def dfs(totalSum,index,arr):
        if totalSum < 0:
            return
        if totalSum == 0:
            result.append(arr)
            return
        for i in range(index, len(cardiates)):
            dfs(totalSum - cardiates[i], i, arr + [cardiates[i]])

    dfs(target,0,[])
    return result

print(CombinationSum(candidates, targetNum))