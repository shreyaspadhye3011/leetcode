
# coding: utf-8

# In[44]:


# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Status: Accepted
# Percentile: 88.03%
# Author: Shreyas Padhye

# Approach: ____
# Further optimizaitons: add in breaks for trivial / end case solutions. When you're sure that no further computation is required.
# Note: All test cases working

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    maxCounter = 1
    currentCounter = 1
    currentList = s[0]
    for i in range(1, len(s)):
        if s[i] in currentList:
            # means it's a reptition. i.e. update header (reference from where currentCounter is maintained), 
            # currentList, check whether maxCounter needs to be updated and update current counter
            foundAt = currentList.index(s[i])
            currentList = currentList[foundAt+1:]   # Caution: check that list[len+1:] doesn't throw exception when "len" is length of list
            
            # set maxCounter if applicable before resetting currentCounter
            if currentCounter > maxCounter:
                maxCounter = currentCounter
            
            # reset counter appropriately
            currentCounter = len(currentList)
        
        # add current element in list in any case
        currentList += s[i]
        currentCounter += 1
    
    if currentCounter > maxCounter:
        maxCounter = currentCounter
    
    return maxCounter
    
# lengthOfLongestSubstring("abcabcbb")   #O: 3
# lengthOfLongestSubstring("abbbbbba")   #O: 2
# lengthOfLongestSubstring("bbbbbb")   #O: 1
# lengthOfLongestSubstring("pwwkew")   #O: 3
# lengthOfLongestSubstring("abbcefghhab")   #O: 6
# lengthOfLongestSubstring("abcdefgh")   #O: 8
# lengthOfLongestSubstring("abcdapqrstuvp")   #O: 11
# lengthOfLongestSubstring("abcdapbdacuvp")   #O: 7
# lengthOfLongestSubstring("abcdea")   #O: 5
# lengthOfLongestSubstring("abcdeafb")   #O: 6
lengthOfLongestSubstring("kfabcdafjbpo")   #O: 8 | cdafjbpo
    
    

