class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        res = []
        rows, cols = len(board), len(board[0])

        def dfs(word: str, count: int, used: list[tuple]) -> bool:
            if len(word) <= count:
                return True
            next_l = word[count]
            curr = used[len(used) - 1]
            r, c = curr[0], curr[1]
            if (r - 1) >= 0:
                if (board[r - 1][c] == next_l and (r - 1, c) not in used):
                    used.append((r - 1, c))
                    return dfs(word, count + 1, used)
                    used.pop()
            if (r + 1) < rows:
                if (board[r + 1][c] == next_l and (r + 1, c) not in used):
                    used.append((r + 1, c))
                    return dfs(word, count + 1, used)
                    used.pop()
            if (c - 1) >= 0:
                if (board[r][c - 1] == next_l and (r, c - 1) not in used):
                    used.append((r, c - 1))
                    return dfs(word, count + 1, used)
                    used.pop()
            if (c + 1) < cols:
                if (board[r][c + 1] == next_l and (r, c + 1) not in used):
                    used.append((r, c + 1))
                    return dfs(word, count + 1, used)
                    used.pop()
            
            return False
        
        for word in words:
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == word[0]:
                        if (dfs(word, 1, [(r, c)]) and word not in res):
                            res.append(word)
        return res