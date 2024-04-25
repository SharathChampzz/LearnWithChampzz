class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        merged_index = m + n - 1

        # As we have to modify the same given array while doing the comparision
        # we will start the comparision from the end, (If we start adding it from the begining, we will loose the data of nums1)
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[merged_index] = nums1[index1]
                index1 -= 1
            else:
                nums1[merged_index] = nums2[index2]
                index2 -= 1
            merged_index -= 1
        
        # if any element left in nums2, add it in the begining of nums1
        while index2 >= 0:
            nums1[merged_index] = nums2[index2]
            index2 -= 1
            merged_index -= 1
            
        # we dont need to run loop for nums1, because the remaining elements are already placed in nums1 in sorted order
        # for example: [1,2,4,0,0,0] [3,5,6] == With the first loop => [1,2,3,4,5,6]

    def Tempmerge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = list(nums1)
        i, j, current_index = 0, 0, 0

        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1[current_index] = nums1_copy[i]
                i += 1
                current_index += 1
            else:
                nums1[current_index] = nums2[j]
                j += 1
                current_index += 1

        while i < m:
            nums1[current_index] = nums1_copy[i]
            i += 1
            current_index += 1

        while j < n:
            nums1[current_index] = nums2[j]
            j += 1
            current_index += 1


