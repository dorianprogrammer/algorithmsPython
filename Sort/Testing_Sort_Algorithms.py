import unittest
from Sort import CountingSort, BucketSort, HeapSort, InsertionSort, RadixSort


class TestingSortAlgorithms(unittest.TestCase):

    def test_insertionsort(self):
        arrayTesting = [10, 45, 23, 1, 67, 2]
        arraySortHoped = [1, 2, 10, 23, 45, 67]
        sortResult = InsertionSort.insertionsort(arrayTesting)
        self.assertEqual(sortResult, arraySortHoped)

    def test_heapsort(self):
        arrayTesting = [10, 45, 23, 1, 67, 2]
        arraySortHoped = [1, 2, 10, 23, 45, 67]
        sortResult = HeapSort.heapsort(arrayTesting)
        self.assertEqual(sortResult, arraySortHoped)

    def test_radixSort(self):
        arrayTesting = ['154', '181', '85', '52', '117', '129', '42', '24', '43', '9']
        arraySortHoped = [9, 24, 42, 43, 52, 85, 117, 129, 154, 181]
        sortResult = RadixSort.radixSort(arrayTesting)
        self.assertEqual(sortResult, arraySortHoped)

    def test_bucketSort(self):
        arrayTesting = [0.42, 0.32, 0.23, 0.53, 0.25, 0.47, 0.51]
        arraySortHoped = [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.53]
        sortResult = BucketSort.bucketSort(arrayTesting)
        self.assertEqual(sortResult, arraySortHoped)

    def test_countingSort(self):
        arrayTesting = [4, 2, 2, 8, 3, 3, 1]
        arraySortHoped = [1, 2, 2, 3, 3, 4, 8]
        sortResult = CountingSort.countingSort(arrayTesting)
        self.assertEqual(sortResult, arraySortHoped)
