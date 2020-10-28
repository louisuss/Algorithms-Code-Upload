from collections import defaultdict

# BF 풀이

# O(n**2)


def palindrome_pairs(words):
    def is_palindrome(word):
        return word == word[::-1]

    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])
    return output

# Trie 풀이


class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = defaultdict(TrieNode)
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]

    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search(self, index, word):
        result = []
        node = self.root

        while word:
            # 3. 탐색 중간에 word_id가 있고(w) 나머지 문자가 팰린드롬인 경우
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 1. 끝까지 탐색했을 때 word_id가 있는 경우(w)
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 2. 끝까지 탐색했을 때 palindrome_word_ids가 있는 경우(p)
        # p 값이 여러개가 될 수 있음. w는 단어의 끙키고 w 이전 노드에 반드시 셋팅.
        # 트라이 삽입 중 남아있는 단어가 팰린드롬이라면 미리 팰린드롬 여부를 세팅
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        return result

# O(n)


class solution:
    def palindrome_pairs(self, words):
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results
