class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for char in ransomNote:
            found = counter.get(char)

            if not found:
                return False

            counter[char] -= 1

        return True