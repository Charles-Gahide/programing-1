# write your code here





def election_winner(votes):
    if not votes:  # empty tuple
        return None
    
    # Step 1: Build tuple of unique candidates
    unique_candidates = ()
    for v in votes:
        if v not in unique_candidates:
            unique_candidates = unique_candidates + (v,)
    
    # Step 2: Manually count votes
    max_votes = 0
    winner = None
    for candidate in unique_candidates:
        count = 0
        for v in votes:   
            if v == candidate:
                count += 1
        
        # Step 3: Track max
        if count > max_votes:
            max_votes = count
            winner = candidate
    
    return winner