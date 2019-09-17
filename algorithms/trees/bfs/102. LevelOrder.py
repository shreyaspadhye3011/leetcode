# Reference: 
# https://www.tutorialspoint.com/python/python_binary_tree.htm
# https://www.youtube.com/watch?v=zaBhtODEL0w

#TODO: Create a method that accepts a list and creates a tree using a complete binary tree input assumtion on the list
#Hint: use the parent index & child index relation

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # BST insertion
    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
    def getChildren(self):
        # update to facilitate for graphs. Currently made for trees. For graphs, it will be done through adjacency list
        if self.left and self.right:
            return [self.left, self.right]
        elif self.left:
            return [self.left]
        elif self.right:
            return [self.right]
        else:
            return None


class Solution():
    def levelOrder(self, root):
        access = [root]
        result = []
        while(len(access) > 0):
            node = access.pop(0)
            childList = node.getChildren()
            if childList:
                result.append(childList)
            for child in childList:
                access.append(child)

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
obj.levelOrder(root)
