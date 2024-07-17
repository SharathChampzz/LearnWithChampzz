class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        occurence_count_1 = Counter([v for v in count1.values()])
        occurence_count_2 = Counter([v for v in count2.values()])

        return count1 == count2 or (occurence_count_1 == occurence_count_2 and set(word1) == set(word2))
