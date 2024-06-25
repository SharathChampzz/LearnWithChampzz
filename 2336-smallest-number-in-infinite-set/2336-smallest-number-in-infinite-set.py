class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1,1010)]
        heapq.heapify(self.heap) # lets have some 10 extra as constraint says. At most 1000 calls will be made in total to popSmallest and addBack.

    def popSmallest(self) -> int:
        return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)