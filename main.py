VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    aces = 0

    # Hand should consist of 2-5 cards, otherwise return 'Invalid'
    if len(hand) > 5 or len(hand) < 2:
        return 'Invalid'
    
    for card in hand:
        # Calculate how many aces are in cards
        if card == 'Ace':
            aces += 1
        # If card is valid calculate cards
        if card in VALID_CARDS:
            # If card is a number, add card
            if isinstance(card, int):
                score += card
            # If card is not a number, add 10
            else:
                score += 10
        # If card is invalid, return 'Invalid
        else:
            return 'Invalid'
        
    # Calculate aces
    for ace in range(aces):
        # If score is less than 10, we can safely add 11
        if score < 10:
            score += 11
        else:
            score += 1
    # If score goes over 21, return 'Bust'
    if score > 21:
        return 'Bust'
    
    return score