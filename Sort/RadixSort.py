def radixSort(list):
    n = 0
    for e in list:
        if len(e) > n:
            n = len(e)

    for i in range(0, len(list)):
        while len(list[i]) < n:
            list[i] = "0" + list[i]

    for j in range(n - 1, -1, -1):
        groups = [[] for i in range(10)]
        for i in range(len(list)):
            groups[int(list[i][j])].append(list[i])
        list = []
        for g in groups:
            list += g
    return [int(i) for i in list]
