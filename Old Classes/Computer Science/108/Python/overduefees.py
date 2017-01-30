CHILD = 'child'
ADULT = 'adult'
SENIOR = 'senior'

def overdue_fees(days_late, age_group):
    """ (int, str) -> number
    
    Return the fees for a book that is days_late days late for a borrower
    in the age group age_group.
    
    >>> overdue_fees(2, SENIOR) # 2 days late, SENIOR borrower
    0.5
    >>> overdue_fees(5, ADULT) # 5 days late, ADULT borrower
    10
    """
    
    if days_late < 4:
        late_fees = days_late * 1
    elif days_late >= 4 and days_late <= 6:
        late_fees = days_late * 2
    elif days_late > 6:
        late_fees = days_late * 3
    
    if age_group == 'child':
        late_fees *= 0.5    
    elif age_group == 'adult':
        late_fees *= 1    
    elif age_group == 'senior':
        late_fees *= 0.25
    
    return late_fees
        