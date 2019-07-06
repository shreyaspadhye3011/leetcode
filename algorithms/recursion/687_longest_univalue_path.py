# Problem: Below leetcode reference modified into finding max depth until which nodes match (not path). Examples from same reference
# Reference: https://leetcode.com/problems/longest-univalue-path/

class Node:
    # max_dep used to keep track of data across Node instances
    max_dep = 0

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
    
    def max_depth(self, dep=0):
        if dep > Node.max_dep:
            Node.max_dep = dep
        
        if self.left != None:
            # if data matches, increase dep or restart count from 0
            if self.left.data == self.data:
                self.left.max_depth(dep+1)
            else:
                self.left.max_depth(0)
                
        if self.right != None:
            # if data matches, increase dep or restart count from 0
            if self.right.data == self.data:
                self.right.max_depth(dep+1)
            else:
                self.right.max_depth(0)
        
        return Node.max_dep

#Example 1: Output: 1
root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(1)
root.right.right = Node(5)

#Example 2: Output: 1
# root = Node(1)
# root.left = Node(4)
# root.right = Node(5)
# root.left.left = Node(4)
# root.left.right = Node(4)
# root.right.right = Node(5)

# root.PrintTree()

ret_val = root.max_depth()
print("Ret val: "+ str(ret_val))
# print("Result: "+ str(Node.max_dep))