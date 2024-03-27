class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store the index so that we can directly shrink the sliding window to set start pointer to index+1
        char_map = {}
        start = 0
        max_length = 0
        
        for end, char in enumerate(s):
            
            # if we find that character was previously encountered, update the start pointer of sliding window
            if char in char_map:
                # update only if the previous duplicate character is present within the current window, else ignore
                if char_map[char] >= start:
                    start = char_map[char] + 1
            char_map[char] = end
            
            max_length = max(max_length, end - start + 1)
            
        return max_length