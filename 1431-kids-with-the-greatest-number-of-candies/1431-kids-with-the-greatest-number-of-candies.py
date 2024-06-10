class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max = max(candies)

        for i, candy_count in enumerate(candies):
            if (candy_count+extraCandies) >= current_max:
                candies[i] = True
            else:
                candies[i] = False

        return candies