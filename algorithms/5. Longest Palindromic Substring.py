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
        s = "strings"
        # s[0] + s[-1]
        # s[1] + s[-2]
        # s[2] + s[-3]
        # s[3] + s[-4]
        # s[-1:]

        max_palindrome = 0
        for i in range(len(s)):
            temp = len(s[i:])
            mid = len / 2
            inner = 0
            while inner < mid:
                back_index = -(i+1)
                if temp[i] == temp[back_index]:
                    inner += 1
                else:
                    break
            if inner == mid:
                if len(temp) > max_palindrome:
                    max_palindrome = len(temp)

        max_palindrome