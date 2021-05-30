def mergeSort(mergeArray):
    if len(mergeArray) > 1:
        arrayOne = mergeArray[:len(mergeArray)//2]
        arrayTwo = mergeArray[len(mergeArray)//2:]

        # recursion
        mergeSort(arrayOne)
        mergeSort(arrayTwo)

        # merge
        i = 0  # index for arrayOne
        j = 0  # index for arrayTwo
        k = 0  # index for mergeArray
        while i < len(arrayOne) and j < len(arrayTwo):
            if arrayOne[i] < arrayTwo[j]:
                mergeArray[k] = arrayOne[i]
                i += 1
            else:
                mergeArray[k] = arrayTwo[j]
                j += 1
            k += 1

        while i < len(arrayOne):
            mergeArray[k] = arrayOne[i]
            i += 1
            k += 1

        while j < len(arrayTwo):
            mergeArray[k] = arrayTwo[j]
            j += 1
            k += 1


arrayTest = [2, 3, 5, 1, 7, 4, 42, 6, 0]
mergeSort(arrayTest)
print(arrayTest)
