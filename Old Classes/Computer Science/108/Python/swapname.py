def swap_name(name_list): 
    """ (list of str) -> NoneType 
 
    name_list contains a single person's name.  Modify name_list so that the first name and last name are swapped. 
                 
    >>> name = ['John', 'Smith'] 
    >>> swap_name(name) 
    >>> name 
    ['Smith', 'John'] 
    >>> name = ['John', 'Andrew', 'Gleeson', 'Smith'] 
    >>> swap_name(name) 
    >>> name 
    ['Smith', 'Andrew', 'Gleeson', 'John'] 
    """ 
    
    if len(name_list) == 2:
        name = name_list[0], name_list[-1] = name_list[-1], name_list[0]
    else:
        name_list[0], name_list[-1] = name_list[-1], name_list[0]
        
        #first_item = L[0]
         #   for i in range(1, len(L)):
          
         #      L[i - 1] = L[i]
        
          #  L[-1] = first_item        
          
""" if __name__ == "__main__"
          
name = ['John', 'Smith'] 
swap_name(name) 
name """