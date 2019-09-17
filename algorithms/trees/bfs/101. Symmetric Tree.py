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
        if (self.left):
            self.left.PrintTree()
        print(self.data)
        if(self.right):
            self.right.PrintTree()
        return

class Solution():
    def is_symmetric(self):
        if self.left and self.right:
            left_tree = self.bfs_none(self.left, "left")
            right_tree = self.bfs_none(self.right, "right")
            if left_tree == right_tree:
                return True
        return False

    def bfs_none(self, direction):
        access = [self]
        pattern = ""
        while(len(access) > 0):
            node = access.pop(0)
            if node:
                pattern += node.data
            else:
                pattern += "None"
            childList = node.getChildren(direction)
            for child in childList:
                # Notice that even None is added as getChildren returns whatever self.left and self.right is
                access.append(child)
        return pattern
    
    def getChildren(self, direction):
        # update to facilitate for graphs. Currently made for trees. For graphs, it will be done through adjacency list
        if (direction == "left"):
            return [self.left, self.right]
        return [self.right, self.left]

# Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)

root = Node(1)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)

root.PrintTree()
root.is_symmetric()

