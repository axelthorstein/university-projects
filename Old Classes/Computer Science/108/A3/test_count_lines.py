import unittest
import poetry_functions

class TestCount_Lines(unittest.TestCase):
    
    def test_count_lines_example_1(self):

        # Test if empty line is given
        actual = poetry_functions.count_lines(['\n'])
        expected = 0
        self.assertEqual(actual, expected)    
    
    def test_count_lines_example_2(self):
        
        # Test if one line is given
        actual = poetry_functions.count_lines(['The first line leads off\n'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_count_lines_example_3(self):
                
        # Test if two lines are given
        actual = poetry_functions.count_lines(['End well\n', 'Be well\n'])
        expected = 2
        self.assertEqual(actual, expected)        

    def test_count_lines_example_4(self):
        
        # Test if more than two lines are given
        actual = poetry_functions.count_lines(['End well\n', 'Be well\n'\
            'Time spent', 'Rhymes spent', 'time will tell'])
        expected = 5
        self.assertEqual(actual, expected)        

    def test_count_lines_example_5(self):
        
        # Test if there are unexpected characters, punctuation, or numerals
        actual = poetry_functions.count_lines(['End well\n\n\n\n', \
            'Be well!!!!!!!\n', '!!!Time spent is 1\n'])
        expected = 3
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)