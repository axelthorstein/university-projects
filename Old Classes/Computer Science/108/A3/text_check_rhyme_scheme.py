import unittest
import poetry_functions

class TestCheck_Rhyme_Scheme(unittest.TestCase):

    def test_check_rhyme_scheme_example_1(self):
        
        # Test if rhyme scheme matches poem
        poem_lines = ['The first line leads off,', \
                  'With a gap before the next.', 'Then the poem ends.']
        actual = ['The first line leads off,', \
                  'With a gap before the next.', 'Then the poem ends.']
        actual_return = poetry_functions.check_rhyme_scheme(poem_lines, \
            ([5, 7, 5], ['A', 'B', 'C']), word_to_phonemes)
        expected = ['The first line leads off,', \
                    'With a gap before the next.', 'Then the poem ends.']
        expected_return = []
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
        
    def test_check_rhyme_scheme_example_2(self):
        
        # Test if rhyme scheme matches all but one is the same as others
        poem_lines = ['The off,', \
                  'With next.', 'Then off.', 'Then off.']
        actual = ['The off,', \
                  'With next.', 'Then off.', 'Then off.']
        actual_return = poetry_functions.check_rhyme_scheme(poem_lines, \
            ([5, 7, 5], ['A', 'B', 'A', 'C']), word_to_phonemes)
        expected = ['The off,', \
                  'With next.', 'Then off.', 'Then off.']
        expected_return = [['The off,', 'Then off.', 'Then off.']]
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
        
    def test_check_rhyme_scheme_example_3(self):
        
        # Test if rhyme scheme matches some but not multiple
        poem_lines = ['The off,', \
                  'With next.', 'Then ends.', 'Then ends.']
        actual = ['The off,', \
                  'With next.', 'Then ends.', 'Then ends.']
        actual_return = poetry_functions.check_rhyme_scheme(poem_lines, \
            ([5, 7, 5], ['A', 'B', 'A', 'C']), word_to_phonemes)
        expected = ['The off,', \
                  'With next.', 'Then ends.', 'Then ends.']
        expected_return = [['The off,', 'Then ends.'], ['Then ends.']]
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
        
    def test_check_rhyme_scheme_example_4(self):
        
        # Test if rhyme scheme none match
        poem_lines = ['The off,', \
                  'With next.', 'Then ends.', 'Then ends.']
        actual = ['The off,', \
                  'With next.', 'Then ends.', 'Then ends.']
        actual_return = poetry_functions.check_rhyme_scheme(poem_lines, \
            ([5, 7, 5], ['A', 'B', 'A', 'B']), word_to_phonemes)
        expected = ['The off,', \
                  'With next.', 'Then ends.', 'Then ends.']
        expected_return = [['The off,', 'Then ends.'], \
                           ['With next.', 'Then ends.']]
        self.assertEqual(actual, expected)
        self.assertEqual(actual_return, expected_return)
    
    #def test_check_rhyme_scheme_example_5(self):
        
        # Test if none are given
        #poem_lines = []
        #actual = []
        #actual_return = poetry_functions.check_rhyme_scheme(poem_lines, \
                #([], ['*', '*', '*']), word_to_phonemes)
        #expected = []
        #expected_return = []
        #self.assertEqual(actual, expected)
        #self.assertEqual(actual_return, expected_return)

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