class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def search1(self, key):  # 탐색연산: 반복구조
        node = self.root
        while node is not None:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def search2(self, key):  # 탐색연산: 재귀
        return self._searchSubtree(self.root, key)

    def _searchSubtree(self, node, key):
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self._searchSubtree(node.left, key)
        else:
            return self._searchSubtree(node.right, key)

    def minimum(self):  # 최소키 반복이용
        node = self.root
        if node is None:
            return None
        while node.left != None:
            node = node.left
        return node.key

    def maximum(self):  # 최대키 반복이용
        node = self.root
        if node is None:
            return None
        while node.right != None:
            node = node.right
        return node.key

    def insert(self, key, value):  # 노드 삽입연산
        self.root = self._insertSubtree(self.root, key, value)

    def _insertSubtree(self, node, key, value):
        if node == None:
            return TreeNode(key, value)
        elif key < node.key:
            node.left = self._insertSubtree(node.left, key, value)
        elif key > node.key:
            node.right = self._insertSubtree(node.right, key, value)
        return node

    def _minNode1(self, node):  # 최소키 노드 찾기 재귀이용
        if node.left == None:
            return node
        else:
            return self._minNode1(node.left)

    def _minNode2(self, node):  # 반복 이용
        if node is None:
            return None
        while node.left != None:
            node = node.left
        return node

    def delete(self, key):  # 삭제 재귀이용
        self.root = self._deleteNode(self.root, key)

    def _deleteNode(self, node, key):
        if node == None:
            return None
        if key < node.key:
            node.left = self._deleteNode(node.left, key)
            return node
        elif key > node.key:
            node.right = self._deleteNode(node.right, key)
            return node
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right

            rightMinNode = self._minNode2(node.right)
            node.key = rightMinNode.key
            node.value = rightMinNode.value
            node.right = self._deleteNode(node.right, rightMinNode.key)
            return node
