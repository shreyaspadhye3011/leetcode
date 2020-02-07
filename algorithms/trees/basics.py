# Reference: 
# https://www.tutorialspoint.com/python/python_binary_tree.htm
# https://www.youtube.com/watch?v=zaBhtODEL0w

#TODO: Create a method that accepts a list and creates a tree using a complete binary tree input assumtion on the list
#Hint: when question realted to BST, you can directly call insert for every element and your tree will be ready
#Hint: use the parent index & child index relation

# bfs: when hierarchy and order of access matters eg right side view of a tree
# dfs: to access all connected nodes to a node eg number of islands

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
    
    def breadthFirstSearch(self):
        access = [self]
        while(len(access) > 0):
            node = access.pop(0)
            # change to search logic if required
            print(node.data)
            childList = node.getChildren()
            for child in childList:
                # comment if you need None in the retrieval
                if child != None:
                    access.append(child)
        return
    
    def getChildren(self):
        # update to facilitate for graphs. Currently made for trees. For graphs, it will be done through adjacency list
        return [self.left, self.right]

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
root.breadthFirstSearch()