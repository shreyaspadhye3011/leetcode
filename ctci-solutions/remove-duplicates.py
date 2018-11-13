# Reference: CTCI
# Author: Shreyas Padhye
# Problem 1.3 (Pg 97) : Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. 
# NOTE: One or two additional variables are fine. An extra copy of the array is not. FOLLOW UP Write the test cases for this method
# Solution Approach: Do a single pass. Create a dictionary to keep track of already passed elements and delete from dictionary if you encounter repeats. Merge dict elements to get string back

# Note: Remember - When you store keys in dictioanry, they are arranged alphabetically
from collections import OrderedDict
class solution():
    def remove_duplicates(self, s):
        d = OrderedDict()

        # single pass, avoid on duplicate entry and add to res string otherwise
        res = ""
        for char in s:
            if char not in d:
                d[char] = True
                res += char
            
        return res
    
t = solution()
t.remove_duplicates("abssateryyv")
t.remove_duplicates("abstr")
t.remove_duplicates("aaaa")
t.remove_duplicates("")
t.remove_duplicates("aaabbb")
t.remove_duplicates("ababab")
