class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        result = None

        total = len(nums1)
        mid = total // 2

        if total % 2 == 0: # if even take average of middle elements
            result = (nums1[mid] + nums1[mid - 1]) / 2
        else: # if old directly pick the middle element
            result = nums1[mid]
        return result