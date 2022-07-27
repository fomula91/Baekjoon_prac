#버블정렬의 알고리즘 구현
def bubblesort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        wall = iters - iter
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur+1] = lst[cur + 1], lst[cur]
    return lst