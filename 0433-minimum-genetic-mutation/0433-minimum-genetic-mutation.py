class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
         Notes:
            Here we have got the start and end, requirement is to find the minimum number of steps required to go to end from start.
            While we dont know the path yet. We should be building the paths and also calculate the minimum steps required,

        Given condition to build new node/path:
            #1. We are allowed to build new node only using ATGC character
            #2. We are allowed to replace only one character at a time
            #3. When building the next node > ensure this node is valid, meaning it should be present in bank
            
            #4. Use BFS algorithm to find the minimum steps required 
        """
        bank = set(bank) # search operation will be faster

        if endGene not in bank:
            return -1 # this mutation is not possible

        # start with initial gene
        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            gene, level = queue.popleft()

            for i in range(8):
                for char in 'ATGC':
                    mutated_gene = gene[:i] + char + gene[i+1:] # modifying only one char is possible

                    if mutated_gene in bank and mutated_gene not in visited:

                        if mutated_gene == endGene:
                            return level + 1

                        queue.append((mutated_gene, level+1))
                        visited.add(mutated_gene)

        return -1