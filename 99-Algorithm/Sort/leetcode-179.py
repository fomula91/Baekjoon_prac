nums = [3,30,34,5,9]
output = "210"

class Solution:
    def largestNumber(self, nums) -> str:
        #반복할 탐색 횟수 [3,30,34,5,9] 일경우 1~4까지 4번반복
        for idx in range(1, len(nums)):
            #탐색 범위 설정
            #5 - 1~4
            cur = len(nums) - idx
            print(f'cur is {cur}')
            #5~1까지 탐색함
            for j in range(cur):
                print(f'j is {j}')
                if str(nums[j+1]) + str(nums[j]) > str(nums[j]) + str(nums[j+1]):
                    print(f'if!!!!!!! {str(nums[j+1]) + str(nums[j])} vs {str(nums[j]) + str(nums[j+1])}')
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                print(f'????????? nums is {nums}')
        #test 케이스중 [0,0]을 위해 int변환
        #최종 아웃풋 str이므로 다시str로 변환
        return str(int(''.join(map(str,nums))))

    
s = Solution()
s.largestNumber(nums)