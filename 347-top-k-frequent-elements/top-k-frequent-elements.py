# import heapq

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         # 1. Count frequency
#         freq = {}

#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1

#         # 2. Min heap
#         heap = []

#         for num, count in freq.items():
#             heapq.heappush(heap, (count, num))

#             # Keep only k elements
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         # 3. Extract elements
#         result = []

#         while heap:
#             count, num = heapq.heappop(heap)
#             result.append(num)

#         return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # buckets[i] contains numbers that appear i times
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Collect from highest frequency to lowest
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
        