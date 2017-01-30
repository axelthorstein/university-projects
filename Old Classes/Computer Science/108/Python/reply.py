def is_reply(reply):
    """(str) -> bool
    
    Return True if and only if this tweet is a reply
    
    >>> is_reply('@cssu Where is your office?')    
    True
    >>> is_reply('Meet the @cssu executive!')
    False
    """
    if ('@') in reply[0]:
        return True
    else:
        return False