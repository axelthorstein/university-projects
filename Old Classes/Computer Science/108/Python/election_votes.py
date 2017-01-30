def election_results(party1_votes, party2_votes):
    """ (list of int, list of int) -> list of int
    Pre-condition: len(party1_votes) == len(party2_votes)
    Return a list of integers representing the number of regions won by each party. The
    first element is the number of regions won by party 1, the second is the number won by
    party 2 and the third is the number of ties. The number of votes for each region are
    in the lists party1_votes and party2_votes, with one entry per region.
    >>> election_results([5, 2, 8], [0, 0, 9])
    [2, 1, 0]
    >>> election_results([17, 13, 40, 100], [18, 10, 40, 0])
    [2, 1, 1]
    """
    result = []
    i = 0
    while i < range(party1_votes):
        if party1_votes[i] > party2_votes[i]:
            result.append(result[0])
        elif party1_votes[i] < party2_votes[i]:
            result.append(result[1])
        else:
            result.append(result[2])
        i = i + 1
    return result
