# https://leetcode.com/submissions/detail/155003210/
class Solution(object):
    # @return an integer
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(curr, cols, main_diag, anti_diag, result):
            row, n = len(curr), len(cols)
            if row == n:
                result.append(map(lambda x: '.'*x + "Q" + '.'*(n-x-1), curr))
                return
            for i in xrange(n):
                if cols[i] or main_diag[row+i] or anti_diag[row-i+n]:
                    continue
                cols[i] = main_diag[row+i] = anti_diag[row-i+n] = True
                curr.append(i)
                dfs(curr, cols, main_diag, anti_diag, result)
                curr.pop()
                cols[i] = main_diag[row+i] = anti_diag[row-i+n] = False
                
        cols = [False]* n
        main_diag = [False]*(2*n)
        anti_diag = [False]*(2*n)
        result = []
        dfs([], cols, main_diag, anti_diag, result)
        return result
