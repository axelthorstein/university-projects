MIN_LENGTH = 1
MAX_LENGTH = 140


def is_valid_tweet(tweet):
    """ (str) -> bool

    Return True if and only if tweet is no less than 1 and no more 
    than 140 characters long.

    >>> is_valid_tweet('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper')
    True
    >>> is_valid_tweet('The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly. - Donald Knuth')
    False
    """
    return len(tweet) >= 1 and len(tweet) <= 140
    
def contains_hash_symbol(tweet):
    """(str) -> bool	
    
    Return True if and only if the tweet contains a hash symbol.

    >>> contains_hash_symbol('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + '# knowledge. - Grace Hopper')
    True
    >>> contains_hash_symbol('The best programs written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand. - Donald Knuth')
    False
    """
    return '#' in (tweet)
    
def is_mentioned(tweet, username):
    """(str, str) -> bool
    
    Return True if and only if the tweet mentions that username preceded by @.

    >>> is_mentioned('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of @gracehopper', 'gracehopper')
    True
    >>> is_mentioned('The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand.', 'Donald Knuth')
    False
    """
    return '@' + username in tweet
    
def report_shortest(tweet1, tweet2):
    """(str, str) -> str
    
    Return 'Tweet 1' if the first tweet is shorter than the second, 
    'Tweet 2' if the second tweet is shorter than the first, and 
    'Same length' if the tweets have the same length.

    >>> report_shortest('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge.', 
        'The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly.')
        Tweet 1
    >>> report_shortest('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper',
        'The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly.')
        Tweet 2   
    >>> report_shortest('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper',
        'The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly.Knuth')
        Same Length
    """
    
    tweet1 = len(tweet1)
    tweet2 = len(tweet2)
    min(tweet1, tweet2)
    if tweet1 < tweet2:
        return("Tweet 1")
    elif tweet1 > tweet2:
        return("Tweet 2")
    else:
        return("Same Length")    
    
def is_reply(reply):
    """(str) -> bool
    
    Return True if and only if this tweet is a reply
    
    >>> is_reply('@cssu Where is your office?')    
    True
    >>> is_reply('Meet the @cssu executive!')
    False
    """
    return ('@') in reply[0]
    
def format_reply_to(username, tweet):
    """(str, str) -> str
    
    Prepare a reply tweet to the given username. 
    If tweet is over 140 characters give an error 
    message with how many characters over
    
    >>> format_reply_to('@cssu', 'Where is your office?')    
    @cssu Where is your office?
    >>> format_reply_to('@cssu', 'Tprogramming is more than an important ' \
        + 'practical art. It is also way to gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper')
    5 characters too long
    """
    if len(username) + len(tweet) <= 140:
        return(username + ' ' + tweet)
    elif len(username) + len(tweet) > 140:
        extra_characters = ((len(username) + len(tweet)) % 140)
        return(str(extra_characters) + ' ' + 'characters too long')
    
    
    import tweet
    import builtins
    
    # Get the initial value of the constant
    constants_before = [tweet.MIN_LENGTH, tweet.MAX_LENGTH]
    
    # Type check tweet.is_valid_tweet
    result = tweet.is_valid_tweet('Test 123')
    assert isinstance(result, bool), \
           '''tweet.is_valid_tweet should return a bool, but returned {0}
           .'''.format(type(result))
    
    # Type check tweet.contains_hash_symbol
    result = tweet.contains_hash_symbol('Test 123')
    assert isinstance(result, bool), \
           '''tweet.contains_hash_symbol should return a bool, but returned {0}.''' \
           .format(type(result))
    
    # Type check tweet.is_mentioned
    result = tweet.is_mentioned('Test 123', 'abc')
    assert isinstance(result, bool), \
           '''tweet.is_mentioned should return an bool, but returned {0}.''' \
           .format(type(result))
    
    
    # Type check tweet.report_shortest
    result = tweet.report_shortest('abc', 'def')
    assert isinstance(result, str), \
           '''tweet.report_shortest should return an str, but returned {0}.''' \
           .format(type(result))
    
    
    # Type check tweet.is_reply
    result = tweet.is_reply('abcd')
    assert isinstance(result, bool), \
           '''tweet.is_reply should return an bool, but returned {0}.''' \
           .format(type(result))
    
    
    # Type check tweet.format_reply_to
    result = tweet.format_reply_to('abcd', 'def')
    assert isinstance(result, str), \
           '''tweet.format_reply_to should return an str, but returned {0}.''' \
           .format(type(result))
    
    
    # Get the final values of the constants
    constants_after = [tweet.MIN_LENGTH, tweet.MAX_LENGTH]
    
    # Check whether the constants are unchanged.
    assert constants_before == constants_after, \
           '''Your function(s) modified the value of constant MIN_LENGTH or
           MAX_LENGTH. Edit your code so that the values of constants are not 
           changed by your functions.'''
