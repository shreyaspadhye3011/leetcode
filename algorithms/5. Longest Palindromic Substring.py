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

        # s = "aabaaba"
        # s[::-1]
        # s = "addaldaaa"
        # s = "asadasaa"
        # s = "addaliladaa"
        # s = "addaladaa"
        s = "aa" 
        # change algo to not break and keep going even if one char mismatches cz there can be some palindrome on the inner side that you can miss

        # s[0] + s[-1]
        # s[1] + s[-2]
        # s[2] + s[-3]
        # s[3] + s[-4]

        # max_palindrome = 0
        # for i in range(len(s)):
        #     temp = s[i:]
        #     temp_len = len(s[i:])
        #     mid = temp_len / 2
        #     inner = 0
        #     curr_counter = 0
        #     back_index = -1
        #     while len(temp[inner:back_index]) > 1:
        #         back_index = -(inner + 1)
        #         if temp[inner] == temp[back_index]:
        #             curr_counter += 1
        #         else:
        #             curr_counter = 0
        #         inner += 1
                
        #     if curr_counter > max_palindrome:
        #         max_palindrome = curr_counter

        # max_palindrome

        ### TODO: handle single char input

        max_palindrome = 0
        max_palindrome_str = ""
        for i in range(len(s)):
            curr_len = 0
            back_index = 0
            check_str = s[i:]
            check_len = len(s[i:])
            while check_len >= 1:
                mid = check_len / 2
                if check_len % 2 == 0:
                    if(check_str[:mid] == check_str[mid:][::-1]):
                        break
                else:
                    if(check_str[:mid] == check_str[(mid+1):][::-1]):
                        break
                back_index -= 1
                check_str = s[i:back_index]
                check_len = len(check_str)

            if check_len > max_palindrome:
                max_palindrome = check_len
                max_palindrome_str = check_str
        return max_palindrome_str