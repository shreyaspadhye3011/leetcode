
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/two-sum/description/
# Status: Approved
# Percentile: 38%
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for indx in range(0, len(nums)):
            if ((target - nums[indx]) in nums and (nums.index(target - nums[indx]) != indx)):
                return [indx, nums.index(target - nums[indx])]
        
twoSum([3, 2, 4], 6)

