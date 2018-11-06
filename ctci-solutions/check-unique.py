# Reference: CTCI
# Author: Shreyas Padhye

# Problem 1.1 (Pg 94): Given a string, check that it has all unique characters

# Solution 1: (extra space allowed): do a single pass and keep storing all items in a dict. If at any point an element already exists in the dict, break. If all elements passed without break, the string has unique elements
#
# Solution 2: (NO extra space allowed): do a single pass through the array and at every element A[i] check that the element does not exist in A[:i], if it does break. If all elements passed without break, the string has unique elements
#
# Questions to ask:
#     1. Is the consideration case sensitive? Currently considered so i.e. `a != A`
class Solution:
    def check_unique_extra_space(self, str):
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
    
    def check_unique_no_extra_space(self, str):
        count = 0
        # TODO: can be improved to nlogn if you sort and just check neighbours. created separate function and implement
        for i in range(0, len(str)):
            if str[i] in str[:i]:
                break
            else:
                count += 1
        if count == len(str):
            return True
        else:
            return False

object = Solution()
object.check_unique_extra_space('abcfd')
        