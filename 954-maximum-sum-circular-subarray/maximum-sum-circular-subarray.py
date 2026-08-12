class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=sum(nums)
        currentMax=0
        maxsum=nums[0]
        currentMin=0
        minsum=nums[0]
        for num in nums:
            currentMax=max(num,currentMax+num)
            maxsum=max(maxsum,currentMax)
            currentMin=min(num,currentMin+num)
            minsum=min(minsum,currentMin)
        if maxsum<0:
            return maxsum
        return max(maxsum,total-minsum)
        