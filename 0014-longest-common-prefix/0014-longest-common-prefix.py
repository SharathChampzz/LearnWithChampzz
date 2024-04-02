class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        prefix_str = ""

        # get smallest string
        small_str = strs[0] # assume first word is smallest
        small_str_len = len(small_str)
        for word in strs[1:]:
            temp_length = len(word)
            if temp_length < small_str_len:
                small_str = word
                small_str_len = temp_length

        # check if prefix exists in all the strings 
        for char_index, char in enumerate(small_str):
            for i in range(length):
                if char != strs[i][char_index]:
                    return prefix_str
            prefix_str += char

        return prefix_str
