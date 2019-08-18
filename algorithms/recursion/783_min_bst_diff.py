# Reference: https://leetcode.com/problems/minimum-distance-between-bst-nodes/ 

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

class Solution():
    first = None
    second = None
    minDiff = 1000000       #any large enough number based on data set or infinity

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return


