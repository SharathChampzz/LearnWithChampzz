class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x,y = 0,0
        small_str_len = len(s)
        big_str_len = len(t)

        # we will iterate through t and check if all the characters from s present in it
        while x < small_str_len and y < big_str_len:
            if t[y] == s[x]:
                x += 1
            y += 1

        return x == small_str_len # x is pointing to end of string means all of the chars from s present in t