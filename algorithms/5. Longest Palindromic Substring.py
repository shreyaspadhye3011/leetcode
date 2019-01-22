# https://leetcode.com/problems/longest-palindromic-substring/
# Status: 
# Percentile: 

# Approach: 

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = "aabaaba"
        # s[0] + s[-1]
        # s[1] + s[-2]
        # s[2] + s[-3]
        # s[3] + s[-4]
        # s[-1:]

        max_palindrome = 0
        for i in range(len(s)):
            temp = s[i:]
            temp_len = len(s[i:])
            mid = temp_len / 2
            inner = 0
            while inner < mid:
                back_index = -(inner + 1)
                if temp[inner] == temp[back_index]:
                    inner += 1
                else:
                    break
            if inner == mid:
                if temp_len > max_palindrome:
                    max_palindrome = temp_len

        max_palindrome