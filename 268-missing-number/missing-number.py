class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
        actualsum=(len(nums)*(len(nums)+1))//2
        missingNum=actualsum-sum
        return missingNum
        