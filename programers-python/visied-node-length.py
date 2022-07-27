from collections import deque, defaultdict

dirs = "ULURRDLLU"

def solution(dirs):
    answer = 0
    test = deque(list(dirs))
    point = deque([])
    stringtoint = deque([])
    goingtoY = [-1,1,0,0]
    goingtoX = [0,0,-1,1]
    charX = 5
    charY = 5

    for i in range(-5, 6):
        temp = []
        for j in range(-5,6):
            temp.append([i,j,False])
        point.append(temp)
    
    # for i in range(0, 11):
    #     for j in range(0,11):
    #         print(point[i][j], end='')
    #     print('')
    while test:
        stringA = test.popleft()
        if stringA == "U": stringtoint.append(0)
        if stringA == "D": stringtoint.append(1)
        if stringA == "L": stringtoint.append(2)
        if stringA == "R": stringtoint.append(3)
    newarr = []
    newdic = defaultdict(int)
    for _ in range(len(list(dirs))):
        # print(len(list(dirs)))
        dir = stringtoint.popleft()
        nextX = charX + goingtoX[dir]
        nextY = charY + goingtoY[dir]
        charX = nextX
        charY = nextY
        prevX = charX - goingtoX[dir]
        prevY = charY - goingtoY[dir]
        
        dicitem = {charX:False}
        for item in dicitem:
            newdic[item]
        print(newarr)
        

        if nextX < 0 or nextY < 0 or nextX >= 11 or nextY >= 11:
            continue
        # print(point[nextX][nextY])
        # print(point[charY][charX][2])
        # print(point[charY][charX])
        if point[charY][charX][2] == False:
            point[charY][charX][2] = True
            point[prevY][prevX][2] = True
            # print(point[prevY][prevX])
            answer += 1
            # print('False!!')
        else: continue
        # print(nextX, nextY)
        
        

    return print(answer)
solution(dirs)