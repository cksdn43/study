def selection_sort(a):  # 선택 정렬
    n = len(a)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if a[j] < a[least]:
                least = j
        a[i], a[least] = a[least], a[i]
        print(a)


def insertion_sort(a):  # 삽입 정렬
    n = len(a)
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        print(a)


def bubble_sort(A):  # 버블 정렬
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
        if not bChanged:
            break
        print(A)


a = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(a)
# selection_sort(a)
# insertion_sort(a)
# bubble_sort(a)
