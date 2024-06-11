class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_vol = 0

        while left < right:
            current_volume = min(height[left], height[right]) * (right - left)
            max_vol = max(max_vol, current_volume)

            # idea is, we will try to get max volume by looking for more heights
            
            # height of left is less so lets move to the next one from left side, If we get more height volume would be more.
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_vol
