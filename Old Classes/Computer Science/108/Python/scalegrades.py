def scale_midterm_grades(grades, multiplier, bonus):
    """ (list of number, number, number) -> NoneType
    
    >>> grades = [45, 50, 55, 95]
    >>> scale_midterm_grades(grades, 1, 10)
    >>> grades
    
    """
    i = 0
    for items in grades:
        if grades[i] < 100:
            grades = grades[i] * multiplier + bonus
            
    for i in range(len(grades)):
        grades[1] = grades[i] * multiplier + bonus
        if grades[i] > 100:
            grades[i] = 100
    for i in range(len(grades)):
        grades[i] = min(grades[i] * multiplier + bonus)
            
    '''while i < len(grades):
        if grades[i] * multiplier + bonus < 100:
            grades[i] = grades[i] * multiplier + bonus
        else:
            grades[i] = 100
        i = i + 1'''