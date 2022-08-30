class MaxHeap:
    def __init__(self):
        self.heap = []

    def printH(self):
        print(self.heap)

    def insert(self, value):  # 최대 힙의 원소 삽입
        self.heap.append(value)
        i = len(self.heap) - 1
        while (i != 0 and value > self.heap[(i-1)//2]):
            self.heap[i] = self.heap[(i-1)//2]
            i = (i-1)//2
        self.heap[i] = value

    def delete(self):  # 최대 힙에서 원소 삭제
        n = len(self.heap)
        if n == 0:
            return None
        current = 0
        maxValue = self.heap[0]  # 최대값 저장
        value = self.heap[n-1]  # 마지막 원소를 value에 저장
        self.heap.pop()  # 마지막 원소 삭제
        n = n - 1  # 원소 하나가 삭제되어 n을 1 줄임
        while (2*current+1 < n):  # current가 leaf가 아니면
            leftChild = 2*current + 1
            rightChild = leftChild + 1
            # 두 자식 노드 중 큰 값의 노드를 largerChild
            if rightChild < n and self.heap[rightChild] > self.heap[leftChild]:
                largerChild = rightChild
            else:
                largerChild = leftChild

            if value < self.heap[largerChild]:  # largerChild의 값이 크면
                self.heap[current] = self.heap[largerChild]
                current = largerChild  # current를 largerChild로 내림
            else:
                break
        self.heap[current] = value
        return maxValue
