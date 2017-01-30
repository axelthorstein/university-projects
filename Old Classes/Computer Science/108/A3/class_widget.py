class widget:

    def __init__(self, name, cost):
        """ (Widget, str, num)

        >>> w = widget('Banana', 2.50)
        >>> w.name
        'Banana'
        >>> w.cost
        2.50
        """

        self.name = name
        self.cost = cost


    def is_cheap(self):
        """ (Widget) -> bool

        Return True if the cost is less than $10, and False otherwise.

        >>> w = widget('Banana', 2.50)
        >>> is_cheap(w)
        True
        >>> w = widget('CD', 12.50)
        >>> is_cheap(w)
        False
        """

        return self.cost < 10.0
