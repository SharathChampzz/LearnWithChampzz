class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Conditions:
            If count == 1: Count shouldnt be mentioned
            If count >= 10: Count should be splitted
        """
        length = len(chars)
        result = []
        iter_index = 0
        chars_i = 0

        while iter_index < length:
            current_char = chars[iter_index]
            count = 0

            while iter_index < length and chars[iter_index] == current_char:
                count += 1
                iter_index += 1

            chars[chars_i] = current_char
            chars_i += 1

            if count != 1:
                for digit in str(count):
                    chars[chars_i] = digit
                    chars_i += 1

        return chars_i