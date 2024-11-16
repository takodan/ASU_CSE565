import unittest
from binarySearchAnomaly import binary_search

class TestBinarySearch(unittest.TestCase):

    myArr = [1, 3, 5, 7, 9, 11, 13]
    def test_case1(self):
        self.assertEqual(binary_search(self.myArr,7), 3)

    def test_case2(self):
        self.assertEqual(binary_search(self.myArr,1), 0)

    def test_case3(self):
        self.assertEqual(binary_search(self.myArr,13), 6)

    def test_case4(self):
        self.assertEqual(binary_search(self.myArr,8), -1)

    def test_case5(self):
        self.assertEqual(binary_search([],1), -1)

if __name__ == '__main__':
    unittest.main()