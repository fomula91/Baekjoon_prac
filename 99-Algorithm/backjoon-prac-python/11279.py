import sys
input = sys.stdin.readline()
num = int(input)
heap = [None]


def sortdown(index):
    biggest = index
    left = 2 * index
    right = 2 * index + 1
    if left <= len(heap)-1 and heap[left] > heap[biggest]:
        biggest = left
    if right <= len(heap)-1 and heap[right] > heap[biggest]:
        biggest = right
    if biggest != index:
        heap[biggest], heap[index] = heap[index], heap[biggest]
        sortdown(biggest)

def sortup():
    if len(heap)-1 > 0:
        cur = len(heap)-1
        parent = cur // 2
        while parent > 0:
            if heap[cur] > heap[parent]:
                heap[cur], heap[parent] = heap[parent], heap[cur]
            cur = parent
            parent = cur // 2

def extract():
    root = heap[1]
    heap[1], heap[-1] = heap[-1], heap[1]
    del heap[-1]
    sortdown(1)
    return print(root)
 
while num > 0:
    getNum = sys.stdin.readline()
    if int(getNum) == 0:
        if len(heap)-1 <= 0:
            print(0)
            num -= 1
            continue
        else:
            extract()
            num -= 1
            continue
    heap.append(int(getNum))
    sortup()
    num -= 1