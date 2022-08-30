def heapify(A, i, n):
    if n == 0:
        return None
    current = i
    value = A[i]
    while 2*current + 1 < n:
        leftChild = 2 * current + 1
        rightChild = leftChild + 1

        if rightChild < n and A[rightChild] > A[leftChild]:
            largerChild = rightChild
        else:
            largerChild = leftChild

        if value < A[largerChild]:
            A[current] = A[largerChild]
            current = largerChild
        else:
            break
    A[current] = value


def makeHeap(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        heapify(A, i, n)


def heapsort(A):
    n = len(A)
    makeHeap(A)

    for last in range(n-1, 0, -1):
        A[last], A[0] = A[0], A[last]
        heapify(A, 0, last)
        print(A)


a = [70, 90, 30, 20, 50, 40, 80, 10, 60]
print(a)
heapsort(a)
print(a)
