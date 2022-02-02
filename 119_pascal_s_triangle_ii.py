class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = list()
        for i in range(rowIndex+1):
            row = list()
            for j in range(i+1):
                cell = 1 if j==0 or j == i else result[i-1][j-1]+result[i-1][j]
                row.append(cell)
            result.append(row)
        return result[-1]