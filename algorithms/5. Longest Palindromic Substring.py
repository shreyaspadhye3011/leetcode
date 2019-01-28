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
        s = "addaldaaa"
        s = "addalidaaa"
        s = "addaliidaaa"
        # s = "aa 
        # change algo to not break and keep going even if one char mismatches cz there can be some palindrome on the inner side that you can miss

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
            curr_counter = 0
            while inner < mid:
                back_index = -(inner + 1)
                if temp[inner] == temp[back_index]:
                    curr_counter += 1
                else:
                    curr_counter = 0
                inner += 1
                
            if curr_counter > max_palindrome:
                max_palindrome = temp_len

        max_palindrome