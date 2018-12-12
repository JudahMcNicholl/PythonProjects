class BSTMap:
    def __init__(self):
        self._root = None
        self._size = 0

    def add(self, key, value):
        node = self.bstSearch(self._root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self._root = self.bstInsert(self._root, key, value, layer=0)
            self._size += 1
            return True

    def bstInsert(self, subtree, key, value, layer):
        if subtree is None:
            subtree = BSTMapNode(key, value, layer)
        elif key < subtree.key:
            subtree.left = self.bstInsert(subtree.left, key, value, layer + 1)
        elif key > subtree.key:
            subtree.right = self.bstInsert(subtree.right, key, value, layer + 1)
        return subtree

    def valueOf(self, key):
        node = self.bstSearch(self._root, key)
        assert node is not None, "Invalid map key."
        return node.value

    def bstSearch(self, subtree, target):
        if subtree is None:
            return None
        elif target < subtree.key:
            return self.bstSearch(subtree.left, target)
        elif target > subtree.key:
            return self.bstSearch(subtree.right, target)
        else:
            return subtree

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def BFS(self, root):
        to_visit = []
        if root:
            to_visit.append(root)
        while to_visit:
            current = to_visit.pop(0)
            yield current
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)


class BSTMapNode:
    def __init__(self, key, value, layer):
        self.key = key
        self.value = value

        self.left = None
        self.right = None

        self.x = layer
        self.y = layer

        self.drawn = False
