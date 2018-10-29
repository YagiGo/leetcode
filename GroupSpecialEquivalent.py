# https://leetcode.com/problems/groups-of-special-equivalent-strings/
from collections import Counter
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        overall_odd_index_list = []
        overall_even_index_list = []
        for word in A:
            odd_index_list = []
            even_index_list = []
            for i in range(len(word)):
                if(i % 2 == 0):
                    even_index_list.append(word[i])
                elif(i % 2 != 0):
                    odd_index_list.append(word[i])
            # print(odd_index_list, even_index_list)
            overall_odd_index_list.append("".join(sorted(odd_index_list)))
            overall_even_index_list.append("".join(sorted(even_index_list)))
        # print(overall_odd_index_list)
        # print(overall_even_index_list)
        odd_counter = Counter(overall_odd_index_list)
        even_counter = Counter(overall_even_index_list)
        reformed_list = [overall_odd_index_list[i]+overall_even_index_list[i] for i in range(len(overall_odd_index_list))]
        return len(Counter(reformed_list))
        # print(reformed_list)
        
        
