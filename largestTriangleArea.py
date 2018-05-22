# https://leetcode.com/problems/largest-triangle-area/description/
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        previous_square = 0
        for combo in list(itertools.combinations(points, 3)):
            a = combo[0]
            b = combo[1]
            c = combo[2]
            len_a = math.sqrt(pow(abs((a[0]-b[0])), 2) +pow(abs((a[1] -b[1])),2))
            len_b = math.sqrt(pow(abs((b[0]-c[0])), 2) +pow(abs((b[1] -c[1])),2))
            len_c = math.sqrt(pow(abs((c[0]-a[0])), 2) +pow(abs((c[1] -a[1])),2))
            mean_len = (len_a + len_b + len_c) /2
            
            try:
                square = math.sqrt(mean_len * abs((mean_len - len_a))*abs((mean_len -len_b))*abs((mean_len - len_c)))
            except:
                print(str(len_a) + ' ' + str(len_b) + ' ' + str(len_c) + ' ' + str(mean_len))
                print(str(a) + str(b) + str(c)) # See where the fuck went wrong
            if square > previous_square:
                previous_square = square
        return previous_square
