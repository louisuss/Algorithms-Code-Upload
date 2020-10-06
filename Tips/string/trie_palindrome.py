from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word[:] == word[::-1]

    def insert(self, index, word):
        node = self.root
        # 단어 뒤집어서 만들기
        for i, char in enumerate(reversed(word)):
            # 단어가 팰린드롬이면 팰린드롬 리스트에 인덱스 추가
            if self.is_palindrome(word[:]):
                node.palindrome_word_ids.append(index)
            
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search(self, index, word):
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            
            if not word[0] in node.children:
                return result
            
            node = node.children[word[0]]
            word = word[1:]
        
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        return result

def palindrome_pairs(words):
    trie = Trie()

    for i, word in enumerate(words):
        trie.insert(i, word)

    result = []
    for i, word in enumerate(words):
        result.extend(trie.search(i, word))
    return result

words = list(input().split())

print(palindrome_pairs(words))
