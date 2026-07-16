class Solution:
    def equalPairs(self, grid):
        row_count = {}

        for row in grid:
            key = tuple(row)
            row_count[key] = row_count.get(key, 0) + 1

        result = 0
        n = len(grid)

        for col in range(n):
            column = []

            for row in range(n):
                column.append(grid[row][col])

            result += row_count.get(tuple(column), 0)

        return result