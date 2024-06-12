class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        str_len = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'} # using set as "in" operator would be faster
        current_count = 0

        # do the calculation for the first window
        for char in s[0:k]:
            if char in vowels:
                current_count += 1

        window_start = 1
        window_end = k
        max_count = current_count

        while window_end < str_len:
            
            # if prev window's last char is vowel, reduce the count
            if s[window_start-1] in vowels:
                current_count -= 1
            # if the new element is vowel, increase the count
            if s[window_end] in vowels:
                current_count += 1

            max_count = max(max_count, current_count)

            window_start += 1
            window_end += 1

        return max_count
