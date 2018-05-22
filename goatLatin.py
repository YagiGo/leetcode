# https://leetcode.com/problems/goat-latin/description/
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        str_list = S.split()
        for word in str_list:
            if word[0] in vowel:
                str_list[str_list.index(word)] = word + 'ma' + 'a' * (str_list.index(word) + 1)
            else:
                str_list[str_list.index(word)] = word[1:] + word[0] + 'ma' + 'a' * (str_list.index(word) + 1)
        return ' '.join(str_list)
            
