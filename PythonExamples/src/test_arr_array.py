"""
Test list-of-list array implementations dict and using tuple subscripting.
"""
import unittest
import arr_array

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr_array.array(N,N,N)
            for i in range(N):
                for j in range(N):
                    for d in range(N):
                        self.assertEqual(a[i,j,d], 0)

    def test_identity(self):
        for N in range(4):
            a = arr_array.array(N,N,N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for d in range(N):
                        self.assertEqual(a[i, j, d], i==j==d)
                    
    def _index(self, a, r, c, d):
        return a[r, c, d]

    def test_key_validity(self):
        a = arr_array.array(10,10,10)
        self.assertRaises(KeyError, self._index, a ,-1, 1,1)
        self.assertRaises(KeyError, self._index, a ,10, 1,1)
        self.assertRaises(KeyError, self._index, a ,1, -1,1)
        self.assertRaises(KeyError, self._index, a ,1, 10,1)

    def test_number_of_elements(self):
            import pprint
            rows = 6
            columns = 6
            depth = 6
            a = arr_array.array(rows, columns, depth)
            for i in range(rows):
                for j in range(columns):
                    for d in range(depth):
                        a[i,j,d] = d
            pprint.pprint(a._data)
            actual_total_elements = len(a._data)
            expected_total_elements = rows * columns * depth
            if actual_total_elements == expected_total_elements:
                    print("Test passes: expected = ",expected_total_elements," Actual = ", actual_total_elements)
            else:
                    print("Test fails: expected = ",expected_total_elements," Actual = ", actual_total_elements)
            self.assertEqual(expected_total_elements,actual_total_elements,"Test fails: expected number of element")

if __name__ == "__main__":
    unittest.main()