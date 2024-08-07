class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Here, we are asked to indentify the distinct number. We have XOR logic where if the bits are same, we will get result as 0. When distinct, we get 1

        Apply XOR on two numbers and if those are same, we will get 0. 

        Also, one main important thing is, a (A ^ B) ^ C = A ^ (B ^ C) ===> order doesnot matter, If any two numbers are same it will nullify (becomes 0)

        Associativite of XOR => In simpler terms, it means that when performing XOR operations on multiple values, the order in which you group them doesn't matter.
        """
        result = 0
        for i in nums:
            result ^= i

        return result

        # Using extra space via hashmap set
        # visited = set()
        # for i in nums:
        #     if i not in visited:
        #         visited.add(i)
        #     else:
        #         visited.remove(i)

        # return visited.pop()

        