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