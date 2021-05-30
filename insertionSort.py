def insertionsort(array):
    key = 0
    i = 0 # index for array
    for j in range(0, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1

        array[i+1] = key

    return array


arrayTest = [31, 41, 59, 26, 41, 58]
insertionsort(arrayTest)
print(arrayTest)
