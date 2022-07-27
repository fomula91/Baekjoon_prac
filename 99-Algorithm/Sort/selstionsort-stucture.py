def selectionsrot(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        for cur in range(iter + 1, len(lst)):
            minimun = cur
        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]
    return lst