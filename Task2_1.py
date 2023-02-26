class Solution:
    def countSquares(self, matrix):
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        count = 0

        for i in range(n):              #Заполняем первую строку и первый столбец
            dp[i][0] = matrix[i][0]
            count += dp[i][0]
        for j in range(1, m):
            dp[0][j] = matrix[0][j]
            count += dp[0][j]

        for i in range(1, n):           #Заполняем остальные ячейки матрицы dp
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    count += dp[i][j]

        return count