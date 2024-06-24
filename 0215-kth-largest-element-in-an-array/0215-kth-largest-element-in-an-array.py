class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # import heapq

        # first, we fill the required k elements to the heap
        min_heap = nums[:k]
        heapq.heapify(min_heap) # modify above list such that of min-heap structure
        
        for i in nums[k:]:
            if i > min_heap[0]:
                # heapq.heappop(min_heap)
                # heapq.heappush(min_heap, i)
                heapq.heappushpop(min_heap, i) # this is more efficient

        return heapq.heappop(min_heap)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     import heapq
    #     min_heap = []
        
    #     for i in nums:
    #         # first we fill the required k elements to the pop
    #         if len(min_heap) < k:
    #             heapq.heappush(min_heap, i)
    #             continue

    #         if i > min_heap[0]:
    #             heapq.heappop(min_heap)
    #             heapq.heappush(min_heap, i)

    #     return heapq.heappop(min_heap)

