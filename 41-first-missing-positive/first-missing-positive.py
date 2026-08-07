class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while(i<n):
            correctIndex=nums[i]-1
            if nums[i]>0 and nums[i]<=n and nums[i]!=nums[correctIndex]:
                nums[i],nums[correctIndex]=nums[correctIndex],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return n+1

        