import sys
import heapq
input1 = int(sys.stdin.readline())
heap = []
result = 0
for i in range(input1):
    inputa = int(sys.stdin.readline())
    heapq.heappush(heap, inputa)
if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
        
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        temp = a+b
        result += temp
        heapq.heappush(heap, temp)

    print(result)

# import heapq
# from sys import stdin

# cards = []
# result = 0

# for i in range(int(stdin.readline())):
#     heapq.heappush(cards, int(stdin.readline()))

# if len(cards) == 1:
#     print(0)
# else:
#     while len(cards) > 1:
#         plus = heapq.heappop(cards) + heapq.heappop(cards)
#         result += plus
#         heapq.heappush(cards, plus)

#     print(result)

# import heapq
# n = int(input())
# heap = []
# for i in range(n):
#     data = int(input())
#     heapq.heappush(heap, data)
# result = 0
# while len(heap) != 1:
#     one = heapq.heappop(heap)
#     two = heapq.heappop(heap)
#     sum_value = one + two
#     result += sum_value
#     heapq.heappush(heap, sum_value)
# print(result)