# Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Approach: on None, return. Keep track of min_depth all throughout. Once processed, min_depth will have answer
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

class Solution():
    def minDepth(self, root):
        if root.left and root.right:
            return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        elif root.right:
            return 1 + self.minDepth(root.right)
        else:
            return 0

# Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)

# Example 2:
root = Node(1)
# depth: 1
root.left = Node(4)
# depth: 2
root.left.left = Node(5)
root.left.right = Node(6)

obj = Solution()
obj.minDepth(root)
