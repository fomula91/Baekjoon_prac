import heapq
import sys

input = sys.stdin.readline()
num = int(input)

heap = []
while num > 0:
    getNum = sys.stdin.readline()
    if int(getNum) == 0:
        if len(heap) <= 0:
            print(0)
            num -= 1
            continue
        else:
            result = heapq.heappop(heap)[1]
            print(result)
            num -= 1
            continue
    heapq.heappush(heap, (-int(getNum), int(getNum)))
    num -= 1