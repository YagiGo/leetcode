# https://leetcode.com/problems/letter-case-permutation/description/
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S.lower()
        res = [""]
        for i in S:
            if ord(i) > 96 and ord(i) < 123:
                res = [c+i for c in res] + [c+i.upper() for c in res]
            else:
                res = [c+i for c in res] 
        return res
