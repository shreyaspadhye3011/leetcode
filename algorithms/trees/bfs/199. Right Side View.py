class solution:
    def rightSideView(self, root):
        dep_dict = {}
        access = [root]
        level_order = [[root]]
        output = []
        dep_dict[root] = 0

        while len(access) != 0:
            node = access.pop()
            child_dep = dep_dict[node] + 1
            for child in self.getChildren(node):
                access.append(child)
                if child_dep >= len(level_order):
                    level_order[child_dep] = [child]
                else:
                    level_order[child_dep].append(child)

        for item in level_order:
            output.append(item[0])
        return output

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# Example 1
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

obj = solution()
obj.rightSideView(root)