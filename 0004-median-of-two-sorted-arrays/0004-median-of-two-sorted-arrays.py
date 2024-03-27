class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        total = len(merged)
        mid = total // 2

        if total % 2 == 0: # if even take average of middle elements
            result = (merged[mid] + merged[mid - 1]) / 2
        else: # if old directly pick the middle element
            result = merged[mid]
            
        return result