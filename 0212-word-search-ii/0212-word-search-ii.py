# from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                node = node.children[char]
            node.word = word

        m, n = len(board), len(board[0])
        result = set()
        visited = set()

        def dfs(i, j, node, word):
            if (i < 0 or i >= m or j < 0 or j >= n or
                (i, j) in visited or not node.children.get(board[i][j])):
                return
            
            visited.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            
            if node.word:
                result.add(node.word)
            
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            
            visited.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        
        return list(result)
