"""
A poetry pattern:  tuple of (list of int, list of str)
  - first item is a list of the number of syllables required in each line
  - second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""

# ===================== Helper Functions =====================

def clean_up(s):
    r""" (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result



# Add your helper functions here.
# ===================== My Helper Functions ===================

def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    """
    
    result = [original]
    
    #For each of the separators create a temporary list. Then for each of the 
    #tokens in the list of  the original string in result, split at the indicated 
    #separator. Then the temporary list replaces the result.  
    
    for sep in separators:
        temp = []
        for fragment in result:
            temp += fragment.split(sep)
            if not temp[-1]:
                temp = temp[:-1]
        result = temp
    return result


def split_and_clean_lines(poem_lines):
    r""" (list of list of str) -> list of str
    
    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends.  As well as all of words in the lines have been split. 
    
    >>> split_and_clean_lines(['The first,', 'With a gap.', 'Then ends.'])
    [['THE', 'FIRST'], ['WITH', 'A', 'GAP'], ['THEN', 'ENDS']]
    >>> split_and_clean_lines(['The first,\n\n', 'With a gap!!!\n'])
    [['THE', 'FIRST'], ['WITH', 'A', 'GAP']]
    """
    
    clean_lines = []
    for line in poem_lines:
        clean_lines.append(clean_up(line))
    
    split_lines = []
    for line in clean_lines:
        split_lines.append(line.split())
    
    final_list = []
    for line in split_lines:
        clean_line = []
        for word in line:
            clean_line += split_on_separators(word, "'")
        final_list.append(clean_line)

    stripped_lines = []
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    for line in final_list:
        new_list = []
        for item in line:
            new_list.append(item.strip(punctuation))
        stripped_lines.append(new_list)
    result = []

    for line in stripped_lines:
        if line:
            result.append(line)
    return result

def count_syllables(poem_lines, word_to_phonemes):
    r""" (list of str, pronunciation dictionary) -> list of int
    
    Count the syllables in each line of a list and return a corresponding 
    list of int to mark syllables in each line. 
    
    >>> poem_lines = ['The first line leads off,', 'Then the poem ends.']
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> count_syllables(poem_lines, word_to_phonemes)
    [5, 5]
    >>> poem_lines = ['The first line leads off,']
    >>> count_syllables(poem_lines, word_to_phonemes)
    [5]
    """
    
    split_lines = split_and_clean_lines(poem_lines)    
        
    # Count the syllables in split_lines and return list
    count_list = []    
    count = 0
    for line in split_lines:
        count = 0
        for word in line:
            for item in word_to_phonemes[word]:
                if item[-1] in '012':
                    count += 1
        count_list.append(count)
        
    return count_list    

def pattern_indices(whole):
    """ (list of list of str, list of str) -> list of list of int, list of list of int
    
    Return a list of list of int that represent the index of rhymes in given 
    lines aw well
    
    
    >>> whole = [['EH1KST', 'AO1F', 'AY1N', 'AO1F'], ['A', 'B', 'B']]
    >>> pattern_indices(whole)
    [[[0], [1, 3], [2]], [[0], [1, 2]]]
    >>> whole = [['EH1KST', 'AO1F'], ['A', 'B', 'A']]
    >>> pattern_indices(whole)
    [[[0], [1]], [[0, 2], [1]]]
    """
    
    # Find the index of each rhyming end syllable and group them together
    # in a list. For all syllables that do not rhyme, put their index in a
    # list by themselves. Do the same for all rhyme indicators and put
    # their indices in a list. Return a list with both groupings. 
    
    return_list = []
    for item in whole:
        rhymes_dict = {}
        count = 0
        for end in item:
            if not end in rhymes_dict.keys():
                rhymes_dict[end] = [count]
            else:
                rhymes_dict[end].append(count)
            count += 1
        value = list(rhymes_dict.values())
        value.sort()
        return_list.append(value)
    return return_list

def get_word_ends(poem_lines, word_to_phonemes):
    r""" (list of str, pronunciation dictionary) -> list of int
    
    Count the syllables in each line of a list and return a corresponding 
    list of int to mark syllables in each line. 
    
    >>> poem_lines = ['The first line leads off,', 'Then the poem ends.']
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> get_word_ends(poem_lines, word_to_phonemes)
    ['AO1F', 'EH1NDZ']
    """
    
    #Get the pronunciation of each last word in the line
    clean_lines = split_and_clean_lines(poem_lines)
    end_words = []
    for item in clean_lines:
        end_words.append(word_to_phonemes[item[-1]])

    # Take only from the last stress to the end of the word
    stresses = []
    for item in end_words:
        index = 0
        for letter in item:
            if letter[-1] in '012':
                last_stress = index
            index += 1
        stresses.append(item[last_stress:])

    # Add all of the stresses together
    word_end = ''
    word_ends = []
    for stress in stresses:
        word_end = ''
        for item in stress:
            word_end += item
        word_ends.append(word_end)
    
    return word_ends

# ===================== Required Functions =====================

def count_lines(lst):
    r""" (list of str) -> int

    Precondition: each str in lst[:-1] ends in \n.

    Return the number of non-blank, non-empty strings in lst.

    >>> count_lines(['The first line leads off,\n', '\n', '  \n',
    ... 'With a gap before the next.\n', 'Then the poem ends.\n'])
    3
    >>> count_lines(['The first line leads off,\n\n\n', '\n', '  \n',
    ... '\n\n\nWith a gap before the next.\n', 'Then the poem ends.\n'])
    3
    >>>
    """
    num_lines = 0
    
    for line in lst:
        clean_lines = clean_up(line) + line[-1]
        clean_lines = clean_lines.split('\n')
        for line in clean_lines:
            new = line.replace(" ", "")
            if new:
                num_lines += 1
            
    return num_lines

def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed 
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n'
    ... + 'With a gap before the next.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    """
    poem_lines = []
    lines = poem.split()
    for line in lines:
        if line:
            poem_lines.append(line)
    return poem_lines
            

def check_syllables(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    syllables for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of syllables, return the empty list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_syllables(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_syllables(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    """ 
    
    count_list = count_syllables(poem_lines, word_to_phonemes)

    result = []
    i = 0
    j = 0
    
    # After the syllables have been counted and put into a list, use the 
    # syllables index to return the lines that are incorrect syllables
    while j < len(pattern[0]):
        if not count_list[i] == pattern[0][j]:
            if pattern[0][i] == 0:
                return result
            else:
                result.append(poem_lines.pop(i))
            i -= 1
        j += 1
        i += 1 

    return result

def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) 
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    >>> poem_lines = ['The first line', 'With a gap before the next.', 'Then the line']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])    
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    []
    """
    # Return empty list for haiku
    count = 0
    for item in pattern[1]:
        if item == '*':
            count += 1
    if count == len(pattern[1]):
        return []
    
    word_ends = get_word_ends(poem_lines, word_to_phonemes)
    
    whole = [word_ends, pattern[1]]    
    pattern_index = pattern_indices(whole)
    
    non_rhyme_lines = []
    shortest_pattern_length = min(len(pattern_index[0]), len(pattern_index[1]))
    for item in [pattern_index[0], pattern_index[1]]:
        if len(item) == shortest_pattern_length:
            shortest_pattern = item
    
    #using the index of     
    
    if pattern_index[0] == pattern_index[1]:
        return []
    else:
        for i in range(len(shortest_pattern)):
            if pattern_index[0][i] != pattern_index[1][i]:
                non_rhyme_line = []
                for item in shortest_pattern[i]:
                    non_rhyme_line.append(poem_lines[item])
                non_rhyme_lines.append(non_rhyme_line)
    
    return non_rhyme_lines

if __name__ == '__main__':
    import doctest
    doctest.testmod()
