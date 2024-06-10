class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True
        
        total_beds = len(flowerbed)
        prev = 0
        current_plot = 0

        while current_plot < total_beds:
            if not (flowerbed[current_plot] or prev):
                # if the plan is not already planted or prev is already planted

                if (current_plot + 1) < total_beds:
                    next = flowerbed[current_plot + 1]
                    if not next: # if next plot is empty, plant it
                        n -= 1
                        flowerbed[current_plot] = 1
                else:
                    if not prev:
                        n -= 1
                        flowerbed[current_plot] = 1

            prev = flowerbed[current_plot]
            current_plot += 1

            if not n: return True
            print(f'n={n} and current_plot={current_plot}')

        return False
            