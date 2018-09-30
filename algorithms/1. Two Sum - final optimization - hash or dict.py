
# coding: utf-8

# In[13]:


# https://leetcode.com/problems/two-sum/description/
# Status: Accepted
# Percentile: 79%
# Author: Shreyas Padhye

# Approach: Only search Arr[indx+1:] for complement to reduce search complexity
# Further optimization options: 
#     a) Use dictionary Implement Hash in python so that the index search is optimized to constant time. Blogs suggest .index() has complexity of O(n)
#     b) keep it neat & store values in variables if you're accessing them more than once eg .index()

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for indx in range(0, len(nums)):
        # print((target - nums[indx]) in d)
        if ((target - nums[indx]) in d):
            return [d[target - nums[indx]], indx]
        d[nums[indx]] = indx

# twoSum([2, 7, 11, 15], 9)
# twoSum([3, 2, 4], 6)
# twoSum([3, 3, 4], 6)
# twoSum([1, 3, 4, 3], 6)
twoSum([3, 3], 6)

