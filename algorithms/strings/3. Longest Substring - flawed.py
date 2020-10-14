
# coding: utf-8

# In[18]:


# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Status: 
# Percentile: 
# Author: Shreyas Padhye

# Approach:

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    maxVal = 1
    for i in range(0, len(s)-1):
        checkStr = s[i+1:]
        if (s[i] in checkStr):   # check to prevent exception in index() when char repitition not found
            curVal = checkStr.index(s[i]) + 1
#             print("Check string is ", checkStr)
#             print("Next ", s[i], " found at ", checkStr.index(s[i]))
#             print("Cur val is: ", checkStr.index(s[i]) + 1)
            if curVal > maxVal:
                maxVal = curVal
        else:
            return len(s[i:])
            # print("Brfeak")
            # this is the largest possible substring, so break after calculating length from i to len
    return maxVal
    
# lengthOfLongestSubstring("abcabcbb")   #O: 3
# lengthOfLongestSubstring("bbbbbb")   #O: 1
# lengthOfLongestSubstring("pwwkew")   #O: 3
# lengthOfLongestSubstring("abbcefghhab")   #O: 9
# lengthOfLongestSubstring("abcdefgh")   #O: 8
# lengthOfLongestSubstring("abcdapqrstuvp")   #O: 12
lengthOfLongestSubstring("abcdapbdacuvp")   #O: 7
    
    

