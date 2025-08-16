from treys import Card, Deck, Evaluator

evaluator = Evaluator()
def monte_carlo_sim(my_hand, known_board, num_players, window_size=500, max_trials=100000):
    wins = 0
    prev_avg = None
    trials =  0

    while trials < max_trials:
        trials+=1

        # Create shuffled deck w/o my cards and board cards
        deck = Deck()
        for card in my_hand + known_board:
            deck.cards.remove(card)
        
        # Deal opponents their cards
        opponent_hands = []
        for a in range(num_players - 1):
            opponent_hands.append(deck.draw(2))
        
        # Deal community cards
        remaining_cards = 5 - len(known_board)
        board = known_board + (deck.draw(remaining_cards) if remaining_cards > 0 else [])

        # Evaluate my hand
        my_score = evaluator.evaluate(board, my_hand)

        # Evaluate opponents hands
        opponent_scores = []
        for hand in opponent_hands:
            opponent_scores.append(evaluator.evaluate(board, hand))
        best_score = min([my_score] + opponent_scores)

        # Count wins/ties
        if my_score == best_score:
            if opponent_scores.count(best_score) == 0:
                wins+=1
            else:
                wins+= 1/(opponent_scores.count(best_score) + 1)
        
        # Check for convergence
        if trials % window_size == 0:
            current_avg = (wins/trials) * 100
            if prev_avg is not None and abs(current_avg - prev_avg) < 0.5:
                break
            prev_avg = current_avg

    return (wins/trials) * 100

while True:
    # Pre-flop
    num_players = int(input("Enter the total number of players: "))
    if num_players == 1:
        continue
    elif num_players == 0:
        break
    my_card1 = input("Enter your first hole card (e.g. As for Ace of Spades): ").strip()
    my_card2 = input("Enter your second hole card (e.g. Td for Ten of Diamonds): ").strip()

    my_hand = [Card.new(my_card1), Card.new(my_card2)]
    print("Your hand is:", Card.int_to_pretty_str(my_hand[0]), Card.int_to_pretty_str(my_hand[1]))

    win_percentage = monte_carlo_sim(my_hand, [], num_players)
    print(f"Estimated winning probability pre-flop: {win_percentage:.2f}%")

    # Post-flop
    num_players = int(input("Enter the number of players still in the hand: "))
    if num_players == 1:
        continue
    elif num_players == 0:
        break
    flop_input = input("Enter the flop cards separated by spaces (e.g. Ah Kd 7s): ").split() # splits the string into a list using spaces as separators
    flop_cards = [Card.new(c.strip()) for c in flop_input] # strip() removes any accidental spaces

    win_percentage = monte_carlo_sim(my_hand, flop_cards, num_players)
    print(f"Estimated winning probability post-flop: {win_percentage:.2f}%")

    # Turn
    num_players = int(input("Enter the number of players still in the hand: "))
    if num_players == 1:
        continue
    elif num_players == 0:
        break
    turn_input = input("Enter the turn card (e.g. Qh): ").strip()
    turn_card = Card.new(turn_input)

    win_percentage = monte_carlo_sim(my_hand, flop_cards + [turn_card], num_players)
    print(f"Estimated winning probability on the turn: {win_percentage:.2f}%")

    # River
    num_players = int(input("Enter the number of players still in the hand: "))
    if num_players == 1:
        continue
    elif num_players == 0:
        break
    river_input = input("Enter the river card (e.g. 5s): ").strip()
    river_card = Card.new(river_input)

    win_percentage = monte_carlo_sim(my_hand, flop_cards + [turn_card, river_card], num_players)
    print(f"Estimated winning probability on the river: {win_percentage:.2f}%")