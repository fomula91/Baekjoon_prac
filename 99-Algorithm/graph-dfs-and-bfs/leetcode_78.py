nums = [1,2,3]
def subset():
    result = []

    def dfs(index,path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i+1, path+[nums[i]])

    dfs(0,[])
    print(result)
    return result


subset()