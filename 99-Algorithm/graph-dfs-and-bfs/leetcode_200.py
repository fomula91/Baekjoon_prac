
#스택으로 구현한 bfs 그래프
def island_dfs_stack(grid):
    #앞뒤 좌우를 탐색할때 사용하는 배열을 미리 만들어놓는다.
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    #row는 gird의 길이 cols는 grid[0]의 길이
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    #위에서 구한 값으로 전체 배열의 요소를 검사
    for row in range(rows):
        for col in range(cols):
            #전체 요소를 검사하는 중에 요소가 1이 아닌경우 아래의 코드를 무시하고 재진행
            if grid[row][col] != '1':
                continue
            
            #그렇지 않은 경우 (요소가 1인경우) cnt를 증가시키고 해당 좌표(요소)를 스택에 추가시킨다.
            cnt += 1
            stack = [(row, col)]

            #스택에 데이터가 있는 한 아래의 코드를 반복한다.
            while stack:
                x, y = stack.pop()
                #스택의 데이터를 꺼내와 x, y변수에 분리 저장한뒤 해당 지점을 0 으로 바꾼다.
                grid[x][y] = '0'
                #앞뒤 좌우를 검사하는 반복문을 추가한다.
                #새로운 x좌표값은 기존 x + 미리 만들어논 배열 =dx[i] 해당 좌표에서 앞뒤 좌우를 검색하기 위해선 해당 좌표 + 1 ~ -1을 더하면 된다.
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                #스택의 데이터를 꺼내와 
                    #찾고자 하는 노드의 node[x]가 마이너 값이거나 row의 값보다 큰경우 or 찾고자하는 노드의 좌우값이 0보다 작거나 cols 보다 큰경우 or grid[nx][ny]값이 1이 아닌경우
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    #스택 추가하는걸 넘긴다.
                    stack.append((nx, ny))
    return cnt


assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3


#재귀 함수를 이용한 문제 풀이방법
def island_dfs_recursive(grid):
    #탐색할 요소의 앞뒤 좌우검색할 배열을 미리 선언
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    #m이 rows/ n이 cols
    m = len(grid)
    n = len(grid[0])
    cnt = 0
    #함수 안에 함수를 사용하여 노드를 검색한다.
    def dfs_recursive(rows, cols):
        #외부에서 받은 데이터 rows가 0보다 작다 or rows가 m보다 크고 or cols가 0보다 작거나 or cols가 n보다 크거나 or 그리드의 좌표가 1이 아닌경우 재귀 함수를 빠져나간다.
        #rows가 0보다 작거나 rows가 m보다 커질수 있나??
        #dx, dy의 값들 때문에 0보다 작아지거나 m보다 커질수도 있다...
        #따라서 아래의 조건은 dx, dy에 의해 0보다 작거나 m,n보다 클경우(배열을 이탈하는 경우)와 gird의 좌표안에 데이터가 0일경우(배열 안 요소의 값이 없을경우) 현재 함수를 이탈한다.

        if rows < 0 or rows >= m or cols < 0 or cols >= n or grid[rows][cols] != '1':
            return

        # 방문처리
        # 최초 좌표에서 상하좌우를 0으로 바꾸면 다음 좌표에서도 이전에 검사했던 항목들이 0으로 되서 재귀 함수를 벗어나게 된다.

        grid[rows][cols] = '0'
        #상하 좌우를 검사해서 만일 데이터가 들어있으면 0으로 바꾸고(방문했다는 처리) 검사를 다하면 빠져나온다.
        for i in range(4):
            dfs_recursive(rows + dx[i], cols + dy[i])
        return
    #row와 col을 계산한다
    for rows in range(m):
        for cols in range(n):
            #rows의 길이인 m과 cols의 길이인 n을 순차로 검사한다.
            #노드라는 변수에 현재 좌표를 넣는다.
            node = grid[rows][cols]
            #만일 현재 노드가 1(데이터가 들어있지 않다면) 아래의 코드를 사용하지 않는다.
            if node != '1':
                continue
            
            #만일 데이터가 들어있다면 카운트를 증가시키고 상하좌우를 검사한다.
            cnt += 1
            dfs_recursive(rows, cols)

    return cnt


assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3