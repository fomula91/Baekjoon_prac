from collections import defaultdict
'''
test case...
# computers = 7
# edge = 6
-> 단방향 그래프 : # dic = defaultdict(None, {1: [2, 5], 2: [3], 3: [], 4: [7], 5: [2, 6], 6: [], 7: []})
-> 양방향 그래프 : # dic = defaultdict(None, {1: [2, 5], 2: [1, 3, 5], 3: [2], 4: [7], 5: [1, 2, 6], 6: [5], 7: [4]})

'''

'''
선언
'''
computers = int(input())
edge = int(input())
network = defaultdict()
visited = []

'''
힘수 선언
'''
def dfs(graph, start, visited):
    visited.append(start)
    global count
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

'''
배열 입력 및 양방향 그래프 입력, 재귀 함수를 사용해 방문 추적
'''
#컴퓨터 수만큼 배열 생성(방문 처리및 간선 표시를 위해)
for i in range(1,computers+1):
    network.setdefault(i, [])
#각 노드 마다 간선 입력...
for i in range(edge):
    a, b = input().split(' ')
    network[int(a)].append(int(b))
    network[int(b)].append(int(a))
#재귀함수 호출(재귀 시작지점)
dfs(network, 1, visited)
#최종 결과
print(len(visited)-1)