class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_freq[:k]]


# through the heap way

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        heap = []
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                if count > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, num))

        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result[::-1]