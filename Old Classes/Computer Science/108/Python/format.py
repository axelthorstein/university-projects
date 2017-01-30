def format_reply_to(username, tweet):
    """(str, str) -> str
    
    Prepare a reply tweet to the given username. If tweet is over 140 characters give an error message with how many characters over
    
    >>> format_reply_to('@cssu', 'Where is your office?')    
    @cssu Where is your office?
    >>> format_reply_to('@cssu', 'To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper')
    5 characters too long
    """
    if len(username) + len(tweet) <= 140:
        return(username + ' ' + tweet)
    elif len(username) + len(tweet) > 140:
        extra_characters = ((len(username) + len(tweet)) % 140)
        return(str(extra_characters) + ' ' + 'characters too long')
        
