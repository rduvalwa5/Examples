'''
arr as dict
'''
import pprint
class array:
    def __init__(self,M,N,D):
        "Create data as dict element"
        self._data = {}
        self._rows = M
        self._cols = N
        self._depth = D
        
    def __getitem__(self,key):
        "Retruns the appropiate element for the two-element subscript tuple"
        row, col, deep = self._validate_key(key)
        try:
            return self._data[row,col,deep]
        except KeyError:
            return 0
        
    def __setitem__(self,key,value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col, deep = self._validate_key(key)
        self._data[row,col,deep] = value
        
    def _validate_key(self, key):
        """Validates a key against the array's shape returning good tuples Raises KeyError"""
        row, col, deep = key
        if (0 <= row < self._rows and
                0 <= col < self._cols and
                0 <= deep < self._depth):
            return key
        raise KeyError("Subscript out of range")
        
        
if __name__ == '__main__':
    import arr_array
    rows = 6
    columns = 6
    depth = 6
    a = arr_array.array(rows, columns, depth)
    for i in range(rows):
        for j in range(columns):
            for d in range(depth):
                    a[i,j,d] = d
#    pprint.pprint(a.__dict__)
    pprint.pprint(a._data)
    actual_total_elements = len(a._data)
    expected_total_elements = rows * columns * depth
    if actual_total_elements == expected_total_elements:
        print("Test passes: expected = ",expected_total_elements," Actual = ", actual_total_elements)
    else:
        print("Test fails: expected = ",expected_total_elements," Actual = ", actual_total_elements)
    