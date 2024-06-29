class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.end_node = False

"""
Trie Tree also called as Prefix Tree, Helpfull in autosuggestion or searching for word. 
Especially when we want to check if a word startswith some char. 
Imagine in a list of 10k words, if we want to check for word starting with "be", Worst situation is word present at the end of the list.
But in Trie Tree, We can reach there in 2 operations.

As, TRIE TREE CONTAINS ATMOST 26 ALPABHET CHARACTERS, look for b -> e -> done
"""

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.childrens:
                curr.childrens[char] = TrieNode()
            curr = curr.childrens[char] # update current pointer to next
        
        curr.end_node = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.childrens:
                return False
            curr = curr.childrens[char]
        return curr.end_node

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.childrens:
                return False
            curr = curr.childrens[char]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)