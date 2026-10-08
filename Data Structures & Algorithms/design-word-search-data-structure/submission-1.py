class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.end_of_word
            
            c = word[i]

            if c == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                else:
                    node = node.children[c]
                    return dfs(i + 1, node)

        return dfs(0, self.root)
