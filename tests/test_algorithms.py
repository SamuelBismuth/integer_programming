"""
Test all supported partition algorithms on small inputs of all supported types.
"""
import integer_programming, unittest
from utils import functions_in_class
import numpy as np

class TestAlgorithms(unittest.TestCase):
    def test_with_list_input(self):

        A = np.array([[1,1,0,0],[0,0,1,1],[1,0,1,0],[0,1,0,1]])
        b = np.array([1,1,1,1])
        c = np.array([0,0,0,0])

        result = integer_programming.steinitz.steinitz_ip(c, A, b)

        assert result == '[1 0 1 0]'

            

if __name__ == "__main__":
    unittest.main()
