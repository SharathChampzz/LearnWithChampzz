class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        length = len(string)

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        # lets solve using two pointer approach
        left = 0
        right = length - 1

        while left < right:
            if string[left] in vowels and string[right] in vowels:
                # swap
                temp = string[left]
                string[left] = string[right]
                string[right] = temp

                left += 1
                right -= 1

            elif string[left] in vowels:
                right -= 1
            else:
                left += 1

        return ''.join(string)
