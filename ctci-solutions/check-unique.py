# Reference: CTCI
# Author: Shreyas Padhye

# Problem: Given a string, check that it has all unique characters

# 1. Approach: (extra space allowed)  do a single pass and keep storing all items in a dict. If at any point an element already exists in the dict. If all elements passed without break, the string has unique elements

class Solution:
    def check_unique(self, str):
        dict = {}
        count = 0
        for char in str:
            if char in dict:
                break
            else:
                dict[char] = True
                count += 1
        
        if count == len(str):
            return True
        else:
            return False

object = Solution()
object.check_unique('abcfd')
        