class TrieNode:
    def __init__(self):
        self.childs = {} # {'char' : 'TrieNode', ...}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.childs:
                curr.childs[char] = TrieNode()
            curr = curr.childs[char]

        curr.end = True

    def search(self, word: str) -> bool:
        nodes = [self.root] # as we need to support dot, we will need to track multiple trienodes

        for char in word:
            if char == '.':
                temp = []
                for node in nodes:
                    temp += list(node.childs.values())
                nodes = temp # collect all trie nodes

            else:
                nodes = [node.childs[char] for node in nodes if char in node.childs]

            if not nodes:
                return False

        return any(node.end for node in nodes)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)