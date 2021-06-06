def bucketSort(array):
    bucket = [[] for i in range(len(array))]
    for j in array:
        index = int(10 * j)
        bucket[index].append(j)
    for k in range(len(array)):
        bucket[k] = sorted(bucket[k])

    a = 0
    for b in range(len(array)):
        for c in range(len(bucket[b])):
            array[a] = bucket[b][c]
            a += 1

    return array

