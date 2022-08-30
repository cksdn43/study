class TNode:  # 트리 노드
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:  # 이진트리
    def __init__(self):
        self.root = None

    def preorder(self):  # 전위 순회
        self._subtreePreorder(self.root)

    def _subtreePreorder(self, p):
        if p is not None:
            print(p.data)
            self._subtreePreorder(p.left)
            self._subtreePreorder(p.right)

    def inorder(self):  # 중위 순회
        self._subtreeInorder(self.root)

    def _subtreeInorder(self, p):
        if p is not None:
            self._subtreeInorder(p.left)
            print(p.data)
            self._subtreeInorder(p.right)

    def postorder(self):  # 후위 순회
        self._subtreePostorder(self.root)

    def _subtreePostorder(self, p):
        if p is not None:
            self._subtreePostorder(p.left)
            self._subtreePostorder(p.right)
            print(p.data)

    def height(self):  # 높이 연산
        return self._subtreeHeight(self.root)

    def _subtreeHeight(self, p):
        if p is None:
            return 0
        else:
            hleft = self._subtreeHeight(p.left)
            hright = self._subtreeHeight(p.right)
            return max(hleft, hright)+1

    def size(self):  # 트리의 노드 개수
        return self._subtreeSize(self.root)

    def _subtreeSize(self, p):
        if p is None:
            return 0
        else:
            return 1 + self.subtreeSize(p.left) + self._subtreeSize(p.right)

    def _subtreeCountLeaf(self, p):  # 트리의 부노드 개수
        if p is None:
            return 0
        elif p.left is None and p.right is None:
            return 1
        else:
            return self._subtreeCountLeaf(p.left) + self._subtreeCountLeaf(p.right)

    def evaluate(self, p):
        if p == None:
            return 0
        else:
            x = self.evaluate(p.left)
            y = self.evaluate(p.right)
            op = p.data
            return  # x op y
