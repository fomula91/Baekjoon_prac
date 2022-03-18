n = 4
k = 2

def combine(n, k):
    results = []
    print('combine')
    def dfs(elements, start, k):
        print(f'dfs start -----------------')
        print(f'elements is {elements}\nstart is {start}\nk is {k}')
        if k == 0:
            results.append(elements[:])
            print('results append!!!!')
            return
        #자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
            print('elements is pop!!!!')
        print(f'dfs end -------------------')
    dfs([], 1, k)
    return results

print(combine(4, 2))