class Event:
    """ A new Calendar Event"""
    
    def __init__(self, start_time, end_time, event_name):
        """ (Event, int, int, str) -> NoneType
        
        Precondition: 0 <= start_time < end_time <= 23
        
        initialize a new event name that starts at start_time, ends at end_time and is named event_name.
        
        >>> e = Event(12, 13, 'Lunch')
        >>> e.start_time
        12
        >>> e.end_time
        13
        >>> e.name
        'Lunch'
        """
        
        self.start_time = start_time
        self.end_time = end_time
        self.name = event_name
        
    def rename(self, new_name):
        """ (Event, str) -> NoneType
        
        Replace the event name with new_name.
        
        >>> e = Event(10, 15, 'Brunch')
        >>> e.rename('Late_Lunch')
        >>> e.name
        'Late_Lunch'
        """
        
        self.name = new_name
        
    def duration(self):
        """ (Event) -> int
        
        Return the duration of this event.
        
        >>> e = Event(10, 15, 'Brunch')
        >>> e.duration()
        5
        """
        
        return (self.end_time - self.start_time)
    
    def __str__(self):
        """ (Event) -> str
        
        Return a string representation of this event.
        
        >>> e = Event(6, 8, 'Exercise')
        >>> str(e)
        'Exercise from 6 to 8'
        """
        
        return "{0} from {1} to {2}".format(self.name, self.start_time, self.end_time)
    
    def __eq__(self, other):
        """ (Event, Event) -> bool
        
        Return True iff this event has the same start_time, end_time,
        and name as other. 
        
        >>> e1 = Event(10, 11, "Comp Sci")
        >>> e2 = Event(10, 11, "Comp Sci")
        >>> e1 == e2
        True
        """
        
        return self.start_time == other.start_time and self.end_time == other.end_time and self.name == other.name
    
    def overlaps(self, other):
        """ (Event, Event) -> bool
        
        Return True iff Event overlaps with other Event.
        
        >>> e1 = Event(10, 14, "Comp Sci")
        >>> e2 = Event(11, 13, "Nap Time")
        >>> e1.overlaps(e2)
        True
        """
        
        return not (self.start_time >= other.start_time or self.end_time <= other.end_time)
    

class Day:
    
    def __init__(self, day = 1, month = 'January', year = 2014):
        """ (Day, int, str, int) - > NoneType
        
         Initialize a day on the calendar with day, month, year, 
         and no events.
         
         >>> d = Day(20, 'September', 1994)
         >>> d.day
         20
         >>> d.month
         'September'
         >>> d.year
         1994
         >>> d.events
         []
        """
        
        self.day = day
        self.month = month
        self.year = year
        self.events = []

    def schedule_event(self, new_event):
        """ (Day, Event) -> bool
        
        schedule a new_event on this day.
        
        >>> d = Day(3, 'December', 2014)
        >>> e = Event(17, 23, 'Celebrate end of classes')
        >>> d.schedule_event(e)
        True
        >>> d.events[0] == e
        True
        """

        for existing_event in self.events:
            if existing_event.overlaps(new_event):
                return False
        self.events.append(new_event)
        return True

    def __str__(self):
        """ (Day) -> str
        
        Return a string representation of this day.
        
        >>> d = Day(20, 'September', 1994)
        >>> d.schedule_event(Event(13, 14, 'Run'))
        True
        >>> d.schedule_event(Event(9, 12, 'Nap'))
        True
        >>> print(d)
        20 September 1994:
        - Run from 13 to 14
        - Nap from 9 to 12
        """
        
        result = '{0} {1} {2}:'.format(self.day, self.month, self.year)
        for item in self.events:
            result += '\n' +  '- ' + str(item)
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    new_years = Day()

    bday = Day(13, 'February')

    first_day = Day(6)

    c_day = Day(1, 'July')
    c_day = Day(month='July')