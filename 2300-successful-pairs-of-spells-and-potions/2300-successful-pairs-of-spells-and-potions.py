class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # Sort potions in ascending order

        pairs = [0] * len(spells)  # Initialize pairs array

        for i, spell in enumerate(spells):
            left, right = 0, len(potions) - 1

            # Binary search to find the first successful pair index
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1  # Move right pointer to find the first successful pair
                else:
                    left = mid + 1

            pairs[i] = len(potions) - left  # Count successful pairs from left onwards

        return pairs