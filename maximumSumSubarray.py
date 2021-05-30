from typing import Match


import math


def MaxConsecutiveSum(array):
    maxSum = array[0]
    currentSum = maxSum

    for i in range(0,len(array)):
        currentSum = max(array[i] + currentSum, array[i])
        maxSum = max(currentSum, maxSum)

    return maxSum


testArray = [-2, 2, 5, -11, 6]
print(MaxConsecutiveSum(testArray))
