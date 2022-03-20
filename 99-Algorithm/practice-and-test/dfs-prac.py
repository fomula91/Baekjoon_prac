gird = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

def numIslands(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cols = len(grid[0])
    rows = len(grid)
    count = 0
    
    def dfs(y,x):
        if x > cols or x < 0 or y > rows or y < 0 or grid[y][x] == "0":
            return
        grid[y][x] = "0"
        for i in range(4):
            dfs(y+dy[i],x+dx[i])
        return
    
    for i in range(rows):
        for j in range(cols):
            node = grid[i][j]
            if node != "1":
                continue
            count += 1
            dfs(i, j)
    print(count)
    return count


numIslands(gird)















# getInput = ""


# def combine(digits):
#     result = []
#     #print(dic[targetString[0]])
#     def bfs(target, start):
#         if len(target) == len(digits):
#             result.append(target)
#             return
#         for i in range(start, len(digits)):
#             for j in dic[digits[i]]:
#                 bfs(target+j, i+1)

#     if not digits:
#         return
#     print(len(result))

#     bfs("", 0)
#     return result
# dic = {"1":"",
#            "2":"abc",
#            "3":"def",
#            "4":"ghi",
#            "5":"jki",
#            "6":"mno",
#            "7":"pqrs",
#            "8":"tuv",
#            "9":"wxyz"}   

# print(combine(getInput))