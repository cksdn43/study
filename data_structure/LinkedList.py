class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def getNode(self, pos):  # pos번째 노드 반환
        if pos < 0:
            return None
        node = self.head  # node는 head부터 시작
        while pos > 0 and node != None:  # pos번 반복
            node = node.link  # node를 다음 노드로 이동
            pos -= 1  # 남은 반복횟수 줄임
        return node  # 최종 노드 반환

    def getEntry(self, pos):    # pos번째 노드의 데이터 반환
        node = self.getNode(pos)    # pos번째 노드
        if node == None:
            return None    # 찾는 노드가 없는 경우
        else:
            return node.data  # 그 노드의 데이터 필드 반환

    # 노드 개수 반환

    def size(self):  # 반복을 이용
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.link
        return count

    def nodeCount(self, node):  # 재귀를 이용
        if node == None:
            return 0
        else:
            return self.nodeCount(node.link) + 1

    def size2(self):
        return self.nodeCount(self.head)

    def delete(self, pos):  # 삭제
        if pos < 0 or pos >= self.size():
            print("위치 error")
            return None
        before = self.getNode(pos - 1)
        if before == None:      # 시작노드 삭제
            elem = self.head.data
            self.head = self.head.link
        else:                   # 중간에 있는 노드 삭제
            elem = before.link.data
            before.link = before.link.link
        return elem

    # 출력

    def printList(self):  # 반복 이용
        node = self.head
        while node != None:
            print(node.data)
            node = node.link

    def printAll(self, node):  # 재귀 이용
        if node is not None:
            print(node.data)
            self.printAll(node.link)

    def printList2(self):
        self.printAll(self.head)

    # 찾기

    def find(self, item):  # 반복 이용
        pos = 0
        node = self.head
        while node is not None:
            if node.data == item:
                return pos
            else:
                pos += 1
                node = node.link
        return -1

    def findLinkedList(self, ptr, item):  # 재귀 이용
        if ptr == None:
            return -1
        elif ptr.data == item:
            return 0
        else:
            pos = self.findLinkedList(ptr.link, item)
            if pos == -1:
                return -1
            else:
                return pos + 1

    def find2(self, item):
        return self.findLinkedList(self.head, item)
