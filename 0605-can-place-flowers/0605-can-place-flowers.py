class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True

        total_beds = len(flowerbed)
        prev = 0
        current_plot = 0

        while current_plot < total_beds:
            already_planted = flowerbed[current_plot]
            
            if already_planted or prev:
                prev = flowerbed[current_plot]
                current_plot += 1
                continue # if the plan is not already planted or prev is already planted
            elif (current_plot + 1) < total_beds:
                next = flowerbed[current_plot + 1]
            else:
                next = 0 # last plot and prev is empty too

            if not next:
                n -= 1
                flowerbed[current_plot] = 1

            prev = flowerbed[current_plot]
            current_plot += 1

            if not n: return True
            print(f'n={n} and current_plot={current_plot}')

        return False
            