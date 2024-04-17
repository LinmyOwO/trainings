class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn.append(x.left)
                if x.right:
                    vn.append(x.right)
            print()
            v = vn

    def __del_leaf(self, child, parent):
        if parent.left == child:
            parent.left = None

        if parent.right == child:
            parent.right = None

    def __del_one_child(self, child, parent):
        if parent.left == child:
            if child.left is None:
                parent.left = child.right
            else:
                parent.left = child.left
        elif parent.right == child:
            if child.left is None:
                parent.right = child.right
            else:
                parent.right = child.left

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


arr = [10, 5, 2, 4, 7, 14, 18, 23, 11]
t = BinaryTree()
for elem in arr:
    t.append(Node(elem))
t.del_node(5)
t.show_wide_tree(t.root)
