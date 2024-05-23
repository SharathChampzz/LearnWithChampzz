class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l # handle case if k > n, avoid rotating again and again

        new_begining = nums[-k:] # the last k number of elements would go to first after right shifting 

        # start moving rest of the elements from middle to the end
        pointer = l-1
        for i in range(l - k - 1, -1, -1):
            nums[pointer] = nums[i]
            pointer -= 1

        # move the last piece to the begining of the list
        for i in range(k):
            nums[i] = new_begining[i]