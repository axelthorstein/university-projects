def sort_team(athlete_to_sport, sport):
    """ (dict of [str: str})
    
    
    """









    team = []
    for athlete in athlete_to_sport:
        if sport in athlete_to_sport[athlete]:
            team.append(athlete)
            
    team.sort()
    
    return team

# team.sort() returns none but stores the answer so NEVER return a list.something statement
            
            
        