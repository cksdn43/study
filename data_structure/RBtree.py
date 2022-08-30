class TNode:
    def __init__(self, color="BLACK", parent=None, left=None, right=None):
        self.color = color
        self.parent = parent
        self.leftchild = left
        self.rightchild = right


class rbtree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):  # 노드 삽입연산
        self.root = self._insertSubtree(self.root, key, value)

    def _insertSubtree(self, node, key, value):
        if node == None:
            return TNode(key, value)
        elif key < node.key:
            node.left = self._insertSubtree(node.left, key, value)
        elif key > node.key:
            node.right = self._insertSubtree(node.right, key, value)
        return node

    def rbInsert(self, x):
        self.insert(x)
        x.color = "RED"
