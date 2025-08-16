## **Motivation**  
I recently got interested in Poker and started watching alot of Poker tournaments and noticed that next to each player was a percentage that updated as the hand progressed.
This percentage is called their equity, i.e. their chance of winning the hand at showdown. For live streamed games, since the viewer and the equity calculator has perfect
information about the cards of all players along with the community cards, the live equity calculator runs very simple computations in order to find the winning odds of each player.
I then wondered that what if there was an equity calculator that estimated the odds of winning from the players perspective (imperfect information) and therefore demonstrated numerically
the risk that each player takes and their confidence in their hand. Not only would this add another layer to poker livestreams but something like this could also be used as a tool to make
decisions with a concrete mathematical edge.

## **How it works**  
To achieve this, it is not feasible to simulate every possible game, given that there are approximately 10^31 possibilities for just a 6 player game. Therefore, I use a monte carlo simulation,
in which I randomly sample games from all the 10^31 possibilities and calculate the percentage of these games that are won by the player. As you increase the number of trials, this percentage
converges to the true probability. I use a poker library called treys which has classes to simulate poker hands and evaluate hand strengths. It has alot of helpful functions such as randomly
drawing a card from a deck, evalutating the quality of a hand, removing cards from a deck, etc.

### Here are some **key features** of the program:  
- Estimates equity for each stage of the game for games with > 2 players (Pre-flop, flop, turn, river)
- Handles ties fairly by splitting equity between tied players
- Uses a convergence check to stop the simulation once the percentage is approximately within 0.5% of the true value

## **How to Use it**  
First you install the treys library, and then u run the program and use it via the CLI.  
It first asks you the number of players, then it asks you your hole cards which you must enter one by one, the format for entering cards is simply *rank* *suit* (with no space in between)  
Ranks: 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A  
Suits: s, c, d, h  
I didn't add any error handling for incorrectly inputting the cards so just make sure you capitalize the ranks T - A and write a lowercase suit, and also be careful not to add duplicate cards because I didn't handle that either.  
At each stage of the game it asks you for more information and gives you your respective odds.  
**When you enter 1 into the number of players left a new hand begins, and when you enter 0, the program ends.**

> Forgive me for not adding any error handling I'm just lazy
