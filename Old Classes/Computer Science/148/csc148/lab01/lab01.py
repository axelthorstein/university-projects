UNDER_20_MINUTES = 19
UNDER_30_MINUTES = 29
UNDER_40_MINUTES = 39
OVER_40_MINUTES = 40

class RaceRegistry:
    """ A 5km RaceRegistry"""
    
    # Use a dictionary to store the runners information
    
    def __init__(self):
        """ (self) -> NoneType
        
        Initialtize a dictionary that organizes the speed catagories of the 
        runners
        
        >>> r = RaceRegistry()
        >>> r.registry
        {}
        """
        self.registry = {'Under_20_Minutes': [], 'Under_30_Minutes': [], 'Under_40_Minutes': [], 'Over_40_Minutes': []}

    def register_runner(self, runner_email, runner_speed):
        """ (self, str, int) -> NoneType
        
        Register a runner in the 5km race by adding there email and 
        Speed catagory to the registry.
        
        >>> r = RaceRegistry()
        >>> r.register_runner('johnsmith@mail.com', 25)
        >>> r.registry
        {40: [], 19: [], 29: ['johnsmith@mail.com'], 39: []}
        """
        if runner_speed <= UNDER_20_MINUTES:
            self.registry['Under_20_Minutes'].append(runner_email)
        elif runner_speed <= UNDER_30_MINUTES:
            self.registry['Under_30_Minutes'].append(runner_email)
        elif runner_speed <= UNDER_40_MINUTES:
            self.registry['Under_40_Minutes'].append(runner_email)   
        else:
            self.registry['Over_40_minutes'].append(runner_email)
    def get_runners(self, speed_catagory):
        """ (self, str) -> list of runners
        
        Return a list of runners in a given legal speed catagory.
        
        >>> r = RaceRegistry()
        >>> r.register_runner('johnsmith@mail.com', 25)
        >>> r.get_runners('Under_30_Minutes')
        ['johnsmith@mail.com']
        """
        
        if speed_catagory in self.registry:
            return self.registry[speed_catagory]
        
      
