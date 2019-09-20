# Problem: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Approach: Modify BFS to a depth based retrieval using dictionary: (either the final result can be depth based dictionary or access can be turned into a dictionary) + add mode parameter to keep track of order for zigzag
# TODO: Add zigzag & depth specific retrieval logic

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
    
    def getChildren(self, mode):
        # update to facilitate for graphs. Currently made for trees. For graphs, it will be done through adjacency list
        if self.left and self.right:
            if mode == "left":
                return [self.left, self.right]
            else:
                return [self.right, self.left]
        elif self.left:
            return [self.left]
        elif self.right:
            return [self.right]
        else:
            return None


class Solution():
    def zigZagOrder(self, root):
        access = [root]
        result = []
        while(len(access) > 0):
            node = access.pop(0)
            #TODO: update mode to be dynamic in call
            childList = node.getChildren("left")
            if childList:
                result.append(childList)
            for child in childList:
                access.append(child)
        return result

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
# root.PrintTree()
# root.breadthFirstSearch()

obj = Solution()
obj.zigZagOrder(root)
