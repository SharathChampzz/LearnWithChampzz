class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string
        min_len = min(len(s) for s in strs)
        low, high = 0, min_len - 1

        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:low]

    def isCommonPrefix(self, strs: List[str], mid: int) -> bool:
        prefix = strs[0][:mid + 1]
        return all(s.startswith(prefix) for s in strs)


        # start_index = 0
        # length = len(strs)
        # prefix_str = ""

        # # get smallest string
        # small_str = strs[0] # assume first word is smallest
        # small_str_len = len(small_str)
        # for word in strs[1:]:
        #     temp_length = len(word)
        #     if temp_length < small_str_len:
        #         small_str = word
        #         small_str_len = temp_length

        # # check if prefix exists in all the strings 
        # for char_index, char in enumerate(small_str):
        #     for i in range(length):
        #         if char != strs[i][char_index]:
        #             return prefix_str
        #     else:
        #         prefix_str += char

        # return prefix_str
