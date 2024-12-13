# The exist method checks if a word can be formed by sequentially adjacent letters in a grid.

# Use DFS to explore all possible paths from each cell.
# Temporarily mark cells as visited with '#' to avoid revisits.
# Backtrack by restoring the cell's original value after recursion.

# Iterate through the grid, starting DFS from each cell.
# Return True if the word is found, otherwise return False.

# TC: O(m * n * 4^L) - m*n cells and 4^L for paths of length L.
# SC: O(L) - Space for the recursion stack.


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False