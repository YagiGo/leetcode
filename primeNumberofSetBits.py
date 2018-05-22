# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
class Solution(object):

    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        """
        res = 0
        for num in range(L, R+1):
            counter = 0
            bin_num_list = list(bin(num).split('b')[1])
            for item in bin_num_list:
                if item == '1':
                    counter += 1
            if self.isPrime(counter):
                res += 1
        return res
        """
        res = 0
        prime_list = [2,3,5,7,11,13,17,19]
        for num in range(L, R+1):
            if bin(num).count('1') in prime_list:
                res += 1
        return res
                
