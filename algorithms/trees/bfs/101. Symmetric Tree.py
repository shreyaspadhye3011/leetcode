# Reference: https://leetcode.com/problems/symmetric-tree/
# Approach 1: Do a BFS on root.left & do a right_BFS (accessed righ to left) on root.right. If both patterns match, it's symmetric
# Possible issues: just bfs order being same doesn't gurantee that it's a mirror. the nodes matching could be in a separate level. 
# Possible solution: do not skip None. When None is included, i.e. a complete binary tree representation is compared, you can be sure that it's symmetric when the pattern matches because you'll match every node

# Approach 2: Compare level by level or Store level by level to be compared 

class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def PrintTree(self):
        
