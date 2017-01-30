def number_of_cents(change):
    """ (int) -> float
    Return the remainder of cents from nearest dollar
    >>> number_of_cents(1.25
    25
    >>> number_of_cents(20.00)
    0
    """
    dollar_remainder = change % 1
    cents = dollar_remainder * 100
    return round(cents)