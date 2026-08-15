class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        xor = 0
        hasNonZero = False

        for num in nums:
            xor ^= num

            if num != 0:
                hasNonZero = True

        if xor != 0:
            return n

        if hasNonZero:
            return n - 1

        return 0