# https://leetcode.com/problems/two-sum/description/
# Satus: Approved
# Percentile: 12%

# coding: utf-8

# In[8]:


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    for outer in range(0, len(nums) - 1):
        for inner in range(outer+1, len(nums)):
            print('Comparing ', nums[outer], ' and ', nums[inner])
            if (nums[outer] + nums[inner] == target):
                return [outer, inner]
        
twoSum([2, 6, 5, 43], 49)
        
        

