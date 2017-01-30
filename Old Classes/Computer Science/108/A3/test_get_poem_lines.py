import unittest
import poetry_functions

class TestGet_Poem_Lines(unittest.TestCase):
    
    def test_get_poem_lines_example_1(self):
        
        actual = poetry_functions.get_poem_lines('The first line,\n\n\n' \
            + 'With a gap before the next.\nThen the poem ends.\n')
        expected = ['The first line,', 'With a gap before the next.', \
            'Then the poem ends.']
        self.assertEqual(actual, expected)

    def test_get_poem_lines_example_2(self):
            
        actual = poetry_functions.get_poem_lines('\n')
        expected = []
        self.assertEqual(actual, expected)    

    def test_get_poem_lines_example_3(self):
        
        actual = poetry_functions.get_poem_lines('!!!!!<>/.>/@#$%%^\n')
        expected = ['!!!!!<>/.>/@#$%%^']
        self.assertEqual(actual, expected)        

    def test_get_poem_lines_example_4(self):
            
        actual = poetry_functions.get_poem_lines('\n\nThe\n\n' + 'time!! \n')
        expected = ['The', 'time!! ']
        self.assertEqual(actual, expected)
    def test_get_poem_lines_example_5(self):
            
        actual = poetry_functions.get_poem_lines('\n' + '\ntime\n' + \
            '!j@h, minu$\n\n\n\n')
        expected = ['time', '!j@h, minu$']
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)