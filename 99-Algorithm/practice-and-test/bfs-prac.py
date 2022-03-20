from collections import deque
graph = { 1 : [2,3,4],
          2 : [5],
          3 : [5],
          4 : [],
          5 : [6,7],
          6 : [],
          7 : [3]}
def bfs_serch(start):
    visited = [start]
    que = deque([start])

    while que:
        node = que.popleft()
        for innode in graph[node]:
            if innode not in visited:
                que.append(innode)
                visited.append(innode)
    return visited

print(bfs_serch(1))