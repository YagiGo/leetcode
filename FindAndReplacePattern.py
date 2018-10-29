"""
Approach 1: Two Maps
Intuition and Algorithm

If say, the first letter of the pattern is "a", and the first letter of the word is "x", then in the permutation, "a" must map to "x".

We can write this bijection using two maps: a forward map \text{m1}m1 and a backwards map \text{m2}m2.

\text{m1} : \text{"a"} \rightarrow \text{"x"} m1:"a"→"x" \text{m2} : \text{"x"} \rightarrow \text{"a"} m2:"x"→"a"

Then, if there is a contradiction later, we can catch it via one of the two maps. For example, if the (word, pattern) is ("aa", "xy"), we will catch the mistake in \text{m1}m1 (namely, \text{m1}(\text{"a"}) = \text{"x"} = \text{"y"}m1("a")="x"="y"). Similarly, with (word, pattern) = ("ab", "xx"), we will catch the mistake in \text{m2}m2.
"""
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: 
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if(m1[w], m2[p]) != (p,w):
                    return False
            return True
        return filter(match, words)
        
