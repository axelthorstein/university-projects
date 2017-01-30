import random
def random_story_generator(training_file, context_length, story_length):
    """ (open file, int, int) -> str
    
    Return a somewhat randomly generated text using the words from the 
    original story. 
    
    >>> random_story_generator('And the fan, and the cup, and the ship, and the fish', 2, 11)
    
    """
    context_to_next_words = build_dictionary(training_file, context_length)
    
    new_story = create_story(context_to_next_words, context_length, num_words)
    
    
def build_dictionary(training_file, context_length):
    """ (open file, int) -> dict
    
    >>> build_dictionary('And the fan, and the cup, and the ship, and the fish', 2)
    """

    #words = open('at', 'r')
    words = training_file.split()
    
    context_to_next_words = {}    
    
    for i in range(len(words) - context_length):
        context = words[i : i + context_length]
        context = tuple(context)
        next_words = words[i + context_length]
        
        if not context in context_to_next_words:
            context_to_next_words[context] = []
        context_to_next_words[context].append(next_words)
    return context_to_next_words

def create_story(context_to_next_words, context_length, num_words):
    """
    create_story(context_to_next_words, 2, 11)
    """
    
    current_context = None
    all_contexts = []
    new_story = ''
    for i in range(num_words):
        if current_context not in context_to_next_words:
            all_contexts = list(context_to_next_words.keys())
            current_context = random.choice(all_contexts)
        possible_words = context_to_next_words[current_context]
        next_word = random.choice(possible_words)
        new_story += ' ' + next_word
        
        current_context = current_context[1:] + (next_word,)
        
    
    for ch in new_story:
        new = new_story[0]
        new.isupper()
        new_story1 = new + new_story[1:]
    
    return new_story[1:]

context_to_next_words = {('the', 'ship,'): ['and'], ('the', 'fan,'): ['and'], ('fan,', 'and'): ['the'], ('ship,', 'and'): ['the'], ('the', 'cup,'): ['and'], ('cup,', 'and'): ['the'], ('and', 'the'): ['cup,', 'ship,', 'fish'], ('And', 'the'): ['fan,']}