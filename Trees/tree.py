class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def get_parent(self):
        return self.parent
    def set_parent(self, parent):
        self.parent = parent

    def get_children(self):
        return self.children
    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(str(self.data)) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def get_postorder_list(self):
        list = []
        self.postorder(self.root, list)
        return list
    def postorder(self, node, list):
        if node is not None:
            for child in node.children:
                self.postorder(child, list)
            list.append(node.data)

    def get_preorder_list(self):
        list = []
        self.preorder(self.root, list)
        return list
    def preorder(self, node, list):
        if node is not None:
            list.append(node.data)
            for child in node.children:
                self.preorder(child, list)

    def get_bfs_tree_list(self):
        list = [self.root]
        stack = [self.root]
        while len(stack) > 0:
            item = stack[0]
            stack.remove(stack[0])
            for child in item.children:
                stack.append(child)
                list.append(child)
        data_list = []
        for item in list:
            data_list.append(item.data)
        return data_list

    def add_node(self, append_node, node_data):
        node = self.find_node(append_node)
        if node is not None:
            child = TreeNode(node_data)
            child.parent = node
            node.children.append(child)
            return child

    def find_node(self, node_data):
        stack = [self.root]
        while len(stack) > 0:
            item = stack.pop()
            if item.data == node_data:
                return item
            else:
                for child in item.children:
                    stack.append(child)
        return None