# def binary_serch(num, target):
#     def bs(start, end):
#         if start > end:
#             return -1
#         mid = (start + end) // 2
#         if num[mid] < target:
#             return bs(mid+1, end)
#         elif num[mid] > target:
#             return bs(start, mid -1)
#         else:
#             return mid
#     return bs(0, len(num) -1)

'''
asert binary_serch(nums=[-1,0,3,5,9,12], target=9) == 4
asert binary_serch(nums=[-1,0,3,5,9,12], target=2) == -1
'''



from bisect import bisect_left, bisect_right


nums = [4,3,9,3,1,9,7,6,9,7]
nums2 = [5,0,8]

class Solution:
    def intersection(self, num1, num2):
        answer = []
        temp = sorted(num1)
        temp2 = sorted(num2)
        result = set()
        for i in range(len(temp)):
            target= temp[i]
            idx = bisect_left(temp2,target)
            
            if idx < len(num2) and target == temp2[idx]:
                result.add(temp2[idx])
            elif len(temp) > i:
                continue
            else:
                return 
        if not answer and not result:
            return 
        answer = list(result)
        return answer
        

        

s= Solution()
print(s.intersection(nums,nums2))


