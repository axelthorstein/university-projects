def add_underscore(s):
    """ (str) -> str
    
    Return a string that contains the characters from s with an underscore 
    added after every character except the last
    
    >>> add_underscore('type')
    t_y_p_e
    >>> add_underscore('written')
    w_r_i_t_t_e_n
    
    """
    result = ''
    
    for ch in s:
        result = result + ch + '_' 
        
    return result[:-1]






