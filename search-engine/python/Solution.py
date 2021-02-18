class SearchEngine:
    """
        Search Engine problem is about implementing a class that supports add and exists operations on words.
        add operation takes in words in lowercase letters (for it is important that it doesn't allow dots, however that too could be handled)
        exists operation takes in words in lowercase letters and dots, where dot matches any character

        Implementation is based on Trie data structure, dot operator is handled by traversing all possible edges in a TrieNode
        not just one.

        Time complexity:
            add - O(|word|)
            exists - depends on how many dots there are, in worst case (very long string of only dots) it is O(Sum of |word|),
                     best case - no dots - it is O(|word|)
        Space complexity: O(Sum of |word|)
    """
    class __Trie:
        class TrieNode:
            def __init__(self):
                self.edges = {}
                self.isWord = False

        def __init__(self):
            self.epsilon = self.TrieNode()
        
        def add(self, word):
            node = self.epsilon
            for c in word:
                if c in node.edges:
                    node = node.edges[c]
                else:
                    node.edges[c] = self.TrieNode()
                    node = node.edges[c]
            node.isWord = True 

        def __exists(self, word, startingNode):
            node = startingNode
            for i in range(len(word)):
                if word[i] == '.':
                    for c in node.edges:
                        if self.__exists(word[i+1:], node.edges[c]):
                            return True
                
                if not word[i] in node.edges:
                    return False
                node = node.edges[word[i]]

            return node.isWord

        def exists(self, word):
            return self.__exists(word, self.epsilon)

    def __init__(self):
        self.trie = self.__Trie()

    def add(self, word):
        assert not '.' in word, ". are not allowed in added words"
        return self.trie.add(word)

    def exists(self, word):
        return self.trie.exists(word)