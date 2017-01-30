def report_shortest(tweet1, tweet2):
    """(str, str) -> str
    
    Return 'Tweet 1' if the first tweet is shorter than the second, 'Tweet 2' if the second tweet is shorter than the first, and 'Same length' if the tweets have the same length.

    >>> report_shortest('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge.', 'The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly.')
        Tweet 1
    >>> report_shortest('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper', 'The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly.')
        Tweet 2   
    >>> report_shortest('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper', 'The best programs are written so that computing ' \
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