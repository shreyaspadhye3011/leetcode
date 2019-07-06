# Problem: Below leetcode reference modified into finding max depth until which nodes match (not path). Examples from same reference
# Reference: https://leetcode.com/problems/longest-univalue-path/

class Node:
    def __init__(self, data=None):

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


class Solution:
    def longestUnivaluePath(self, root):
        self.ans = 0
        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.data == node.data:
                left_arrow = left_length + 1
            if node.right and node.right.data == node.data:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
    
# def max_unival_path(node):
#     if node == None:
#         return 0
    
#     if node.left == node.right:
#         return max_unival_path(node.left) + max_unival_path(node.left)
#     return

#Example 1: Output: 1
# root = Node(5)
# root.left = Node(4)
# root.right = Node(5)
# root.left.left = Node(1)
# root.left.right = Node(1)
# root.right.right = Node(5)

#Example 2: Output: 1
# root = Node(1)
# root.left = Node(4)
# root.right = Node(5)
# root.left.left = Node(4)
# root.left.right = Node(4)
# root.right.right = Node(5)

#Example 3: Output: 2
root = Node(1)
root.left = Node(4)
root.right = Node(1)
root.left.left = Node(4)
root.right.left = Node(1)
root.right.right = Node(1)


root.PrintTree()
obj = Solution()
print(obj.longestUnivaluePath(root))

# ret_val = root.max_depth()
# print("Ret val: "+ str(ret_val))
# print("Result: "+ str(Node.max_dep))