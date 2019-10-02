# Reference: https://leetcode.com/problems/minimum-depth-of-binary-tree/

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
        result = [[root.data]]
        depth_dict = {}
        depth_dict[root] = 0
        mode = "left"
        while(len(access) > 0):
            node = access.pop(0)
            #TODO: update mode to be dynamic in call
            depth = depth_dict[node] + 1
            childList = node.getChildren(mode)
            if childList:
                for child in childList:
                    access.append(child)
                    depth_dict[child] = depth
                    # append to result array when first entry of depth level
                    if depth == len(result): 
                        result.append([child.data])
                    # append at depth when entry already exists
                    else:
                        if depth % 2 != 0:
                            result[depth].append(child.data)
                        else:
                            # TODO: check whether creating list and then reversal is better than this (check complexity of insert or can even do `7 + [1, 2, 3]``)
                            result[depth].insert(0, child.data)
        return result

# Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)

# Example 2:
root = Node(1)
# depth: 1
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)
# Output: [[1], [4], [6, 5]]

obj = Solution()
obj.zigZagOrder(root)
