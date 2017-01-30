##########  Provided helper function. ############

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """
    
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result

##########        My Helper Functions         ############

def split_and_cleaned_tokens(s):
    """ (list of str) -> list of str
    
    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. As well as splitting
    the string into seperate strings of only words. 
    
    >>> split_and_cleaned_tokens(['James More Cooper\n', 'Peter Parker\n'])
    ['james', 'more', 'cooper', 'peter', 'parker']
    >>> split_and_cleaned_tokens(["Axel, try me?\n', 'Wiheba it'll be.\n"])
    ['axel', 'try', 'me', '', 'wiheba', "it'll", 'be']
    """
    
    # Create a new list, taking each string and splitting it into tokens
    # and then cleaning each token. Return the list of split and clean tokens
    cleaned_words = []
    for subtext in s:
        for item in subtext.split():
            cleaned_words.append(clean_up(item))
    return cleaned_words

def extract_sentences(text):
    """ (list of str) -> list of str
    
    Precondition: text contains at least one sentence.
    
    Return a list of sentences determined by terminating punctuation marks 
    ".?!" from a list of strings. 
    
    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> extract_sentences(text)
    ['The time has come, the Walrus said\n To talk of many things: \
    of shoes - and ships - and sealing wax,\n Of cabbages; and kings.\n', \
    ' And why the sea is boiling hot;\n and whether pigs have wings.\n']
    >>> text = ['Can you come with me? She said quietly.', \
    'I cannot. I said.']
    >>> extract_sentences(text)
    """
    
    #Append all items into one string
    sentence = ''
    for item in text:
        sentence += item.strip() + ' '
    
    sentence = sentence.strip()    
    
    result = split_on_separators(sentence, '.?!')
    return result
        
text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    
def split_and_cleaned_sentences(text):
    """ (list of str) -> list of list of str
    
    Return a list of list of strings that have been split into tokens and 
    if a token itself is a punctuation character it is removed.
    
    >>> text = ['The time has come, the Walrus said.\n',
        'And whether pigs have wings.\n']
    >>> split_and_cleaned_sentences(text)
        [['The', 'time', 'has', 'come,', 'the', 'Walrus', 'said.'], 
        ['And', 'whether', 'pigs', 'have', 'wings.']]
    """
    
    #Extract sentences from the text
    result = extract_sentences(text)
    
    #Split the text into tokens
    end_result = []   
    for item in result:
        end_result.append(item.split())
    
    #If a token is a string with one character of punctuation, then remove
    # it from the list
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    for sentence in end_result:
        for token in sentence:
            if token in punctuation:
                sentence.remove(token)
                
    #Return a list of list of sentences in tokens
    return end_result

##########  Complete the following functions. ############

def avg_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text. 
    
    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143 
    """    
    
    # Split and clean tokens and put into new list
    count = split_and_cleaned_tokens(text)
    result = 0.0
    g = 0.0
    
    # Count each letter in each token and add it to the result. Also keep a 
    # counter 'g' to keep track of how many letters there are. Then divide by 
    # the total amount of words. 
    for ch in count:
        for i in ch:
            result = result + float(len(i))
        g = g + 1.0
    return (result / g)
    

def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    """
  
    count = split_and_cleaned_tokens(text)
    
    # Create a list of split and cleaned tokens and for each token if it is 
    # not in the new list, append it. Then divide the amount of tokens by
    # the total number of words. 
    token = []
    for item in count:
        if item not in token:
            token.append(item)
    return len(token) / len(count)
         
def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of 
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    """
    
    # Keep two lists; one for the unique words, and one with all of the words
    words = split_and_cleaned_tokens(text)    
    single_words = []
    
    # Add each word if it isn't in the single_word list, however if it 
    #appears a second time remove it both from the single_words list.
    for word in words:
        if not word in single_words:
            single_words.append(word)
        else:
            single_words.remove(word)
            
    # Return the amount of single_words divided by the total amount of words. 
    return len(single_words) / len(words)

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
                
def avg_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.
    
    A sentence is defined as a non-empty string of non-terminating 
    punctuation surrounded by terminating punctuation or beginning or 
    end of file. Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.   

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5
    """
    
    list_of_sentences = split_and_cleaned_sentences(text)
    num_tokens = 0   
    for sentence in list_of_sentences:
        num_tokens += len(sentence)
    
    return num_tokens / len(list_of_sentences)  
    
def avg_sentence_complexity(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.    

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    """
    phrases = []
    result = 0
    
    # Divide the text into sentences, then into phrases based on the 
    # punctuation and add to a new list called phrases
    sentences = extract_sentences(text)
    for sentence in sentences:
        phrases.append(split_on_separators(sentence, ",:;"))
    
    # Count the number of phrases in each sentence and add the number to
    # result
    for i in range(len(phrases)):
        result += len(phrases[i])
        
    # Divide the number of phrases by the number of sentences and return the 
    # result
    return result / len(sentences)   

def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two 
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.
    
    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    """
    
    # As long as the weight is greater than zero, subtract the corresponding
    # sig values and multiply the absolute value by the weight. Add all
    # together and return
    result = 0
    i = 0
    while i < len(sig1):
        if weight[i] == 0:
            i += 1
        else:
            result += abs(sig1[i] - sig2[i]) * weight[i]
            i += 1
    return result  