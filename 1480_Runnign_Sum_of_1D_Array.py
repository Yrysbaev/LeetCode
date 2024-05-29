class Solution(object):
    def runningSum(self, nums):

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        print(nums)



Solution = Solution()
Solution.runningSum(nums=[1,2,3,4])