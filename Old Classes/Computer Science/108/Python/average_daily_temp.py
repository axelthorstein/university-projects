def average_daily_temp(high_temps, low_temps):
    """ (list of number, list of number) -> list of float

    Precondition: len(high_temps) == len(low_temps)

    high_temps and low_temps are daily high and low temperatures for a series
    of days. Return a new list of temperatures where each item is the daily
    average.
   
    >>> average_daily_temp([26, 27, 27, 28, 27, 26], [20, 20, 20, 20, 21, 21])
    [23.0, 23.5, 23.5, 24.0, 24.0, 23.5]
    """
    result = []
    i = 0
    while i < len(high_temps):
        result.append((high_temps[i] + low_temps[i]) * 0.5)
        
        i = i + 1
        
    return result
        
        