class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []

        word_len = len(words[0])
        window_size = word_len * len(words)
        counter = Counter(words)

        for i in range(len(s)-window_size+1):
            sub_str = s[i:i+window_size]
            split_sub_str = [sub_str[j:j+word_len] for j in range(0, window_size, word_len)]

            if Counter(split_sub_str) == counter:
                result.append(i)

        return result


    def TempfindSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []

        from itertools import permutations
        substrings = []

        # generate the permutations 
        for perm in permutations(words):
            substrings.append("".join(perm))

        print(substrings)

        full_length = len(s)
        substring_length = len(words[0])*len(words)

        for index in range(full_length-substring_length+1):
            if s[index:index+substring_length] in substrings:
                result.append(index)

        return result

        