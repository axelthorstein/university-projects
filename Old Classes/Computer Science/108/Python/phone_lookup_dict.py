def reverse_lookup_dictionary(phone_num, phone_to_name):
    """ (str, dict of {str: str}) -> str

    This function receives a phone number phone_num, and a dictionary
    phone_to_name in which each key is a phone number and each value
    is the name associated with that phone number.
	
    Return the name associated with phone_num in phone_to_name, or
    an empty string if there is no match.
    
    >>> reverse_lookup_dictionary("416-555-3498", {"416-555-3498": \
        "John A. Macdonald", "647-555-9812": "Louis Riel", "416-555-6543": \
        "Canoe Head", "905-555-6681":"Tim Horton"})
    'John A. Macdonald'        
    """

    if phone_num in phone_to_name.keys():
        return phone_to_name[phone_num]
    return ''
    
