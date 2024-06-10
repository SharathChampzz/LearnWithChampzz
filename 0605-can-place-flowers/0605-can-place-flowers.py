class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True
        
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] or flowerbed[i] or flowerbed[i+1]:
                continue
            flowerbed[i] = 1
            n -= 1
            
            if not n: return True
            
        return False
 