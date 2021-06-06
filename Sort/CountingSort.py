def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    for j in range(1, 10):
        count[j] += count[j - 1]

    a = size - 1
    while a >= 0:
        output[count[array[a]]-1] = array[a]
        count[array[a]] -= 1
        a -= 1

    for k in range(0, size):
        array[k] = output[k]

    return array
