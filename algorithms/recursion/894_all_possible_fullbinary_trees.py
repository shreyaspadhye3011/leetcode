# Reference: https://leetcode.com/problems/all-possible-full-binary-trees/
# Approach: Draw trees starting from n = 3 and realize that:
# 1. full binary trees only possible with odd numbers
# 2. solution of 'n' can be retrieved by number of all children in solution 'n-2'
# 3. **Special: When n = 3, 7, 15, 31... => there will be a problem of duplicate counting of full binary trees  if we accept all children (draw and check). Handle that case.

import math

class Solution():
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 'n' has no solution when it is even
        if n < 1 or n % 2 == 0:
            return 0
        if n == 1 or n == 3:
            return 1
        # TODO: Put this list check in a separate function or logic
        if n not in [3, 7, 15, 31, 63]:
            return self.allPossibleFBT(n-2) * self.calculateLeafCount(n-2)
        else:
            return self.allPossibleFBT(n-2) * self.calculateLeafCount(n-2) - self.calculateDuplicate(n-2) 
    
    # formula created out of observation
    def calculateLeafCount(self, n):
        return int(n/2) + 1
    
    # formula created out of observation
    def calculateDuplicate(self, n):
#         print(pow(2, int(math.log(n,2)) - 1))
        return pow(2, int(math.log(n,2)) - 1) - 1

obj = Solution()
# obj.allPossibleFBT(3)   # output: 1
# obj.allPossibleFBT(5)   # output: 2
# obj.allPossibleFBT(7)   # output: 5
# obj.allPossibleFBT(9)   # output: 20
obj.allPossibleFBT(11)   # output: 100


