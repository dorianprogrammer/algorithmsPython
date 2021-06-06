def max_heap(array, n, parent_index):
    largest = parent_index
    left = 2 * parent_index + 1
    right = 2 * parent_index + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != parent_index:
        array[largest], array[parent_index] = array[parent_index], array[largest]
        max_heap(array, n, largest)


def heapsort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        max_heap(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        max_heap(array, i, 0)

    return array
