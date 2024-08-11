class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        str_len = len(s)

        status = [False] * (str_len + 1)
        status[-1] = True # we are exactly at end

        for i in range(str_len-1, -1, -1):
            temp = []

            for word in wordDict:
                substr_len = len(word)

                if (i + substr_len) > str_len:
                    continue # it will overflow

                if s[i: i+substr_len] == word:
                    temp.append(status[i+substr_len]) # we can stop here actually if any one is found
            
            if any(temp):
                status[i] = True

        return status[0]





























    def InternetwordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        wordSet = set(wordDict)
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[n]
