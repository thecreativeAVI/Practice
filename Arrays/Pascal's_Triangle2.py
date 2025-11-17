class Solution(object):
    def getRow(self, rowIndex):
        result = []

        for i in range(rowIndex+1):
            # Start each row with 1
            row = [1] * (i + 1)
            # Fill in the middle elements
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)

        g=result[::-1]
        return (g[0])
