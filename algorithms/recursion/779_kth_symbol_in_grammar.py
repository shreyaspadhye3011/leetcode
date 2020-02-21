# Reference: https://leetcode.com/problems/k-th-symbol-in-grammar/
# Approach: Notice the pattern: 
# For row m, when m is even, pattern(m-1) is taken & !(pattern(m-1)) is appended to get value of row m
# when m is odd, pattern(m-1) is taken & rev(pattern(m-1)) is appended to get value of row m

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        res = nth_row(N)
        print(res)
        return int(res[K-1])
    
    def nth_row(n):
        if n == 1:
            return "0"
        p = nth_row(n-1)
        # if n is even, append complement of prev sequence
        if n % 2 == 0:
            return p + ''.join([str((int(c) ^ 1)) for c in p])
        # if n is odd, append reverse of prev sequence
        else:
            return p + p[::-1]

obj = Solution()
obj.kthGrammar(5, 2)

