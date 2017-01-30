import unittest
import poetry_functions

class TestCheck_Syllables(unittest.TestCase):

    def test_check_syllables_example_1(self):
        
        # Test if two lines don't match but one does
        actual = ['The first line leads off,', \
                  'With a gap before the next.', 'Then the poem ends.']
        actual_return = poetry_functions.check_syllables(poem_lines, \
            pattern, word_to_phonemes)
        expected = ['The first line leads off,', \
                    'With a gap before the next.', 'Then the poem ends.']
        expected_return = ['With a gap before the next.', \
                           'Then the poem ends.']
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
        
    def test_check_syllables_example_2(self):
        
        # Test if syllables don't matter for one line.
        poem_lines = ['The first line leads off,']
        actual = ['The first line leads off,']
        actual_return = poetry_functions.check_syllables(poem_lines, \
                ([0], ['*']), word_to_phonemes)
        expected = ['The first line leads off,']
        expected_return = []
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
        
    def test_check_syllables_example_3(self):
        
        # Test when all lines match the same syllable count
        poem_lines = ['The first line,', 'With a gap.', 'The poem.']
        actual = ['The first line,', 'With a gap.', 'The poem.']
        actual_return = poetry_functions.check_syllables(poem_lines, \
                ([3, 3, 3], ['*', '*', '*']), word_to_phonemes)
        expected = ['The first line,', 'With a gap.', 'The poem.']
        expected_return = []
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
        
    def test_check_syllables_example_4(self):
        
        # Test when multiple don't match syllable count
        poem_lines = ['The first line,', 'With a gap.', 'The poem.']
        actual = ['The first line,', 'With a gap.', 'The poem.']
        actual_return = poetry_functions.check_syllables(poem_lines, \
                ([5, 6, 5], ['*', '*', '*']), word_to_phonemes)
        expected = ['The first line,', 'With a gap.', 'The poem.']
        expected_return = ['The first line,', 'With a gap.', 'The poem.']
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
    
    def test_check_syllables_example_5(self):
        
        # Test if multiple syllables don't matter for multiple lines
        poem_lines = ['The first line,', 'With a gap.', 'The poem.']
        actual = ['The first line,', 'With a gap.', 'The poem.']
        actual_return = poetry_functions.check_syllables(poem_lines, \
                ([0, 0, 0], ['*', '*', '*']), word_to_phonemes)
        expected = ['The first line,', 'With a gap.', 'The poem.']
        expected_return = []
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
            
poem_lines = ['The first line leads off,', \
        'With a gap before the next.', 'Then the poem ends.']
pattern = ([5, 5, 4], ['*', '*', '*'])
word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'], \
                    'GAP': ['G', 'AE1', 'P'], \
                    'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'], \
                    'LEADS': ['L', 'IY1', 'D', 'Z'], \
                    'WITH': ['W', 'IH1', 'DH'], \
                    'LINE': ['L', 'AY1', 'N'], \
                    'THEN': ['DH', 'EH1', 'N'], \
                    'THE': ['DH', 'AH0'], \
                    'A': ['AH0'], \
                    'FIRST': ['F', 'ER1', 'S', 'T'], \
                    'ENDS': ['EH1', 'N', 'D', 'Z'], \
                    'POEM': ['P', 'OW1', 'AH0', 'M'], \
                    'OFF': ['AO1', 'F']}
if __name__ == '__main__':
    unittest.main(exit=False)