class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

root = Node(1)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)

root2 = Node(1)
root2.left = Node(4)
root2.right = Node(10)
root2.left.left = Node(4)
root2.left.right = Node(4)
root2.right.right = Node(5)


obj = Solution()
obj.isSameTree(root, root2)
    