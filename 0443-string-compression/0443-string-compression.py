class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compresses the string in-place and returns the new length of the array.
        
        Conditions:
            - If count == 1: Count should not be mentioned.
            - If count >= 10: Count should be split into individual characters.
        """
        n = len(chars)
        write_index = 0  # Index to write the compressed characters
        read_index = 0  # Index to read the original characters

        while read_index < n:
            current_char = chars[read_index]
            count = 0

            # Count occurrences of the current character
            while read_index < n and chars[read_index] == current_char:
                count += 1
                read_index += 1

            # Write the character to the array
            chars[write_index] = current_char
            write_index += 1

            # Write the count to the array if it's more than 1
            if count > 1:
                count_str = str(count)
                chars[write_index:write_index + len(count_str)] = count_str
                write_index += len(count_str)

        return write_index