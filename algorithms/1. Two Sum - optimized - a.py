
# coding: utf-8

# In[20]:


# https://leetcode.com/problems/two-sum/description/
# Status: Accepted
# Percentile: 39.5%

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
    for indx in range(0, len(nums)):
#         print(nums[indx+1:])
#         print((target - nums[indx]) in nums[indx+1:])
#         print(nums.index(target - nums[indx]) != indx)
        if ((target - nums[indx]) in nums[indx+1:]):
#             nums.index(target - nums[indx]) != indx -- required for case [3, 2, 4] i.e when a single number can match itself,our logic will fail as we want two distinct complements
#                 print(nums[indx+1:])
                return [indx, (nums[indx+1:].index(target - nums[indx]) + len(nums[:indx+1]))]

twoSum([2, 7, 11, 15], 9)
# twoSum([3, 2, 4], 6)
# twoSum([3, 3, 4], 6)
# twoSum([1, 3, 4, 3], 6)
# twoSum([3, 3], 6)

