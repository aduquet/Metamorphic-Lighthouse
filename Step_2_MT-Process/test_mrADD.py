import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

from mrADD import MR_ADD, _ttd

class TestMR_ADD(unittest.TestCase):
    def test_td_list(self):
        # Test _ttd with a list
        result = _ttd([1, 2, 3], 2)
        self.assertEqual(result, [3, 4, 5])

    def test_td_int(self):
        # Test _ttd with an integer
        result = _ttd(5, 2)
        self.assertEqual(result, 7)

    def test_followUP(self):
        # Test the followUP method
        mr_add = MR_ADD(6, 6, [1, 3], [4], 1, 2, 3, [])
        result = mr_add.followUP(2)
        expectedKeys = ['td_1_mr_add', 'td_2_mr_add', 'td_3_mr_add', 
                        'td_4_mr_add', 'td_5_mr_add', 'td_6_mr_add', 
                        'td_7_mr_add', 'td_8_mr_add', 
                        'ttd_1_mr_add', 'ttd_2_mr_add', 'ttd_3_mr_add', 
                        'ttd_4_mr_add', 'ttd_5_mr_add', 'ttd_6_mr_add', 
                        'ttd_7_mr_add', 'ttd_8_mr_add']
        keys = list(result.keys())
        
        self.assertEqual(expectedKeys, keys)
    
    def test_followUP2(self):
        # Test the followUP method
        mr_add = MR_ADD(6, 6, [1, 3], [4], 1, 2, 3, [])
        results = mr_add.followUP(2)

        # Create the expected DataFrame
        columns = ['td_1_mr_add', 'td_2_mr_add', 'td_3_mr_add', 
                   'td_4_mr_add', 'td_5_mr_add', 'td_6_mr_add', 
                   'td_7_mr_add', 'td_8_mr_add', 
                    'ttd_1_mr_add', 'ttd_2_mr_add', 'ttd_3_mr_add',
                    'ttd_4_mr_add', 'ttd_5_mr_add', 'ttd_6_mr_add',
                    'ttd_7_mr_add', 'ttd_8_mr_add']
        row = [6, 6, [1, 3], [4], 1, 2, 3, [],
               8, 8, [3, 5], [6], 3, 4, 5, []]
        
        expected = pd.DataFrame(columns=columns)
        expected.loc[0] = row
        
        # Compare the actual results with the expected DataFrame
        # print(results)
        # print('=====')
        # print(expected)
        assert_frame_equal(results, expected)

            

        # Add assertions here to check the DataFrame and other results

if __name__ == '__main__':
    unittest.main()