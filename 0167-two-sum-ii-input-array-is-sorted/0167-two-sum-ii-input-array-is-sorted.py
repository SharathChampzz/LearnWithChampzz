class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # constant space by using two pointer approach
        length = len(numbers)
        left, right = 0, length - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1 # we need some higher number to reach the target try with next available higher number
            else:
                right -= 1 # total has become high try some less number

        return [-1, -1]
        

    def twoSumOnSpace(self, numbers: List[int], target: int) -> List[int]:
        mapper = defaultdict(int)

        for index, i in enumerate(numbers):
            compliment = target - i

            if compliment in mapper:
                return [mapper.get(compliment)+1, index+1]
            else:
                mapper[i] = index