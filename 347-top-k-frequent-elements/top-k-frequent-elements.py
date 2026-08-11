import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1. Count frequency
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # 2. Min heap
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            # Keep only k elements
            if len(heap) > k:
                heapq.heappop(heap)

        # 3. Extract elements
        result = []

        while heap:
            count, num = heapq.heappop(heap)
            result.append(num)

        return result