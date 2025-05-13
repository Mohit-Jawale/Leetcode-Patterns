class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = []

class Trie:
    def __init__(self, row, col):
        self.ROW = row
        self.COL = col
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word.append(word)

    def search(self, r, c, board):
        curr = self.root
        ans = set()
        visited = set()

        def dfs(r, c, curr):
            if not (0 <= r < self.ROW and 0 <= c < self.COL):
                return
            if (r, c) in visited:
                return

            char = board[r][c]
            if char not in curr.children:
                return

            curr = curr.children[char]
            if curr.end_of_word:
                for word in curr.end_of_word:
                    ans.add(word)

            visited.add((r, c))

            dfs(r + 1, c, curr)
            dfs(r - 1, c, curr)
            dfs(r, c + 1, curr)
            dfs(r, c - 1, curr)

            visited.remove((r, c))

        dfs(r, c, curr)
        return ans

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_search_trie = Trie(len(board), len(board[0]))

        for word in words:
            word_search_trie.insert(word)

        ans = set()

        for row in range(len(board)):
            for col in range(len(board[0])):
                ans.update(word_search_trie.search(row, col, board))

        return list(ans)
