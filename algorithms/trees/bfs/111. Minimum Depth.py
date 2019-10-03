# Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Approach: on Leaf, return. As you go lower down in recursive call, keep adding depth
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
            # when it has no children. Leaf case
            return 0

# Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)

# # Example 1:
# root = Node(1)
# # depth: 1
# root.left = Node(4)
# # depth: 2
# root.left.left = Node(5)
# root.left.right = Node(6)
# Outupt: 2

# Example 2:
root = Node(1)
# depth: 1
root.left = Node(4)
root.right = Node(5)
# depth: 2
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)
# depth: 3
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.left.right.right = Node(9)
root.right.right.left = Node(10)
# depth: 4
root.left.left.left.left = Node(11)
root.left.left.left.right = Node(12)
root.left.left.right.right = Node(13)
root.right.right.left.left = Node(14)
root.right.right.left.right = Node(15)
# Output: 3

obj = Solution()
obj.minDepth(root)
