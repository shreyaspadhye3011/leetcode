# Reference: https://leetcode.com/problems/range-sum-of-bst/
# Approach: Recursively visit every node and calculate sum. Use BST features to skip lower nodes of out of bounds nodes

class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


class Solution:
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, low, high, node):
        if node == None:
            return

        if node.data >= low and node.data <= high:
            self.sum += node.data
#             print("##########")
#             print(node.data)
#             print(self.sum)
#             print("##########")
            self.rangeSumBST(low, high, node.left)
            self.rangeSumBST(low, high, node.right)
        elif node.data <= low:
            self.rangeSumBST(low, high, node.right)
        else:
            self.rangeSumBST(low, high, node.left)
        return self.sum
    

#Example 1: 
# root = Node(41)
# root.left = Node(38)
# root.right = Node(55)
# root.left.left = Node(30)
# root.right.left = Node(42)
# root.right.right = Node(60)
# root.left.left.left = Node(18)
# root.left.left.right = Node(32)
# root.right.right.left = Node(58)
# root.right.right.left.right = Node(66)
# # root.PrintTree()
# obj = Solution()
# print(obj.rangeSumBST(40, 70, root))  # output: 322
# print(obj.rangeSumBST(1, 70, root))  # output: 440
# print(obj.rangeSumBST(32, 43, root))  # output: 153
# print(obj.rangeSumBST(0, 0, root))  # output: 153


#Example 2: 
# root = Node(10)
# root.left = Node(5)
# root.right = Node(15)
# root.left.left = Node(3)
# root.left.right = Node(7)
# root.right.right = Node(18)
# obj = Solution()
# print(obj.rangeSumBST(7, 15, root))  # output: 32

#Example 3: 
# root = Node(10)
# root.left = Node(5)
# root.right = Node(15)
# root.left.left = Node(3)
# root.left.right = Node(7)
# root.right.left = Node(13)
# root.right.right = Node(18)
# root.left.left.left = Node(1)
# root.left.right.left = Node(6)
# obj = Solution()
# print(obj.rangeSumBST(6, 10, root))  # output: 23

#Example 4: 
root = Node(1)
root.right = Node(12)
obj = Solution()
print(obj.rangeSumBST(1, 12, root))  # output: 13