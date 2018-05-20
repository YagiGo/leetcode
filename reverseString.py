# https://leetcode.com/problems/reverse-string-ii/description/
"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters 
counting from the start of the string. If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if(k >= len(s)):
            return s[::-1]
        start_pos = 0
        end_pos = k
        res = []
        while end_pos < len(s):
            res.append(s[start_pos:end_pos][::-1])
            start_pos += 2*k
            print(start_pos)
            print(end_pos)
            if(start_pos > len(s)):
                start_pos = end_pos + 1
                res.append(s[end_pos:len(s)])
                break
            else:
                res.append(s[end_pos:start_pos])
            if start_pos + k >= len(s):
                res.append(s[start_pos:len(s)][::-1])
                end_pos = len(s)
            else:
                end_pos = start_pos + k
        return ''.join(res)
        
