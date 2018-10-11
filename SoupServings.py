# https://leetcode.com/problems/soup-servings
class Solution(object):
    def soupServings(self, N):
        visited = {}
        def helper(soup_A, soup_B):
            if (soup_A, soup_B) not in visited:
                if soup_A <= 0 or soup_B <= 0:
                    return (soup_A < soup_B and 1) or (soup_A==soup_B and 0.5) or 0
                else:
                    visited[(soup_A,soup_B)] = 0.25 * (helper(soup_A-100, soup_B) + helper(soup_A-75, soup_B-25) + helper(soup_A -50, soup_B - 50) + helper(soup_A -25, soup_B -75))
                    return visited[(soup_A,soup_B)]
            else:
                return visited[(soup_A,soup_B)]
        return (N>4800 and 1) or round(helper(N, N), 5)
            
