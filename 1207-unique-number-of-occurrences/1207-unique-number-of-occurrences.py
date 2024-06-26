class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = defaultdict(int)
        unique_counts = set()

        for i in arr:
            occurences[i] += 1
            unique_counts.add(occurences[i])
            # print(f'Occurences: {occurences}, UniqueCounts: {unique_counts}')

        return len(occurences) == len(set(occurences.values())) # remove the duplicates from count values, and see if the length still remain same.