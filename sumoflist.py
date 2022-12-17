class Solution:
    def runningSum(self, nums):
        ls = []
        sum = 0
        for i in range(len(nums)):
            sum = sum +nums[i]
            ls.append(sum)
        return ls

