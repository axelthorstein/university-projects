"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    lines = pronunciation_file.readlines()
    pro_dict = {}
    
    for line in lines:
        if not line.startswith(';;;'):
            split_line = line.split()
            pron_names = split_line[0]
            syllables = split_line[1:] 
            pro_dict[pron_names] = syllables

    return pro_dict

def read_poetry_form_description(poetry_forms_file):
    """ (file open for reading) -> poetry pattern

    Precondition: we have just read a poetry form name from poetry_forms_file.

    Return the next poetry pattern from poetry_forms_file.
    """
    file = poetry_forms_file
    line = file.readline()
    syllables = []
    rhyme = []
    space_index = line.index(' ')
    
    while line != '\n':
        if line == '':
            return (syllables, rhyme,)         
        syllables.append(int(line[0:space_index]))
        rhyme.append(line[space_index + 1: -1])
        line = file.readline()
          
    return (syllables, rhyme,)
    

def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
    poetry_forms_dict = {}
    form_name = poetry_forms_file.readline()[:-1]
    while form_name != '':
        poetry_forms = read_poetry_form_description(poetry_forms_file)    
        poetry_forms_dict[form_name] = poetry_forms
        form_name = poetry_forms_file.readline()[:-1]

    return poetry_forms_dict
