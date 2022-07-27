#퀵소트의 구현

def quickSort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1
        for j in range(ps, pe):
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]
        part[i+1], part[pe] = part[pe], part[i+1]
        return i + 1
    if start >= end:
        return None
    p = partition(lst, start, end)
    quickSort(lst, start, p - 1)
    quickSort(lst, p + 1, end)
    return lst