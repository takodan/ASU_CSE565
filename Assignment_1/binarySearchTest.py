import unittest
from binarySearch import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_case1(self):
        arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
        self.assertEqual(binary_search(arr,219), 2)

    def test_case2(self):
        arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
        self.assertEqual(binary_search(arr,218), -1)


    arr_one = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
    
    def test_case3(self):
        self.assertEqual(binary_search(self.arr_one,104), 0)

    def test_case4(self):
        self.assertEqual(binary_search(self.arr_one,980), 19)

    def test_case5(self):
        self.assertEqual(binary_search(self.arr_one,572), 9)

    def test_case6(self):
        arr_one_mod = self.arr_one[:-1]
        # print(arr_one_mod)
        self.assertEqual(binary_search(arr_one_mod,572), 9)

    myArr = [1, 3, 5, 7, 9, 11, 13]
    def test_case7(self):
        self.assertEqual(binary_search(self.myArr,7), 3)

    def test_case8(self):
        self.assertEqual(binary_search(self.myArr,1), 0)

    def test_case9(self):
        self.assertEqual(binary_search(self.myArr,13), 6)

    def test_case10(self):
        self.assertEqual(binary_search(self.myArr,8), -1)

    def test_case11(self):
        self.assertEqual(binary_search([],1), -1)

if __name__ == '__main__':
    unittest.main()