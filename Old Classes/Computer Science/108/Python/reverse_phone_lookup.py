def reverse_lookup_lists(phone_num, phone_numbers, names):
    """ (str, list of str, list of str) -> str

    Precondition: len(phone_numbers) == len(names)

    This function receives a phone number phone_num, and two lists: a list of 
    phone numbers phone_numbers and a list of names names.  These lists are
    parallel lists, so the name in position 0 of the names list is 
    associated with the phone number in position 0 of the phone_numbers 
    list, and so on.

    Return the name associated with phone_num according to phone_numbers
    and names, or an empty string if there is no match.
    
    >>> reverse_lookup_lists('416-555-6543', ['416-555-3498', \
        '647-555-9812', '416-555-6543', '905-555-6681'], ['John A. Macdonald', \
        'Louis Riel', 'Canoe Head', 'Tim Horton'])        
    'Canoe Head'
    """
    
    result = ''
    i = 0
    while i < len(phone_numbers):
        if phone_numbers[i] == phone_num:
            result += names[i]
        i = i + 1
        
    return result