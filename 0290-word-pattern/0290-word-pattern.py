class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_to_char = {}
        char_to_word = {}
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        for char, word in zip(pattern, words):
            if char not in char_to_word and word not in word_to_char:
                char_to_word[char] = word
                word_to_char[word] = char
            elif char in char_to_word and char_to_word[char] != word:
                return False
            elif word in word_to_char and word_to_char[word] != char:
                return False

        return True
