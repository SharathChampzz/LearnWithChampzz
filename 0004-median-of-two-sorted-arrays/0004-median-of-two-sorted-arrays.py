class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2) # remove duplicates and sort

        total = len(merged)
        mid = total // 2

        if len(merged) % 2 == 0:
            result = (merged[mid] + merged[mid - 1]) / 2
        else:
            result = merged[mid]
            
        return result