from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums, k):
        freq = Counter(nums)

        ans = 0

        for num, count in freq.items():
            if count % k == 0:
                ans += num * count

        return ans