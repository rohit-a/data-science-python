# Snakes and Ladders

In a classic game of Snake and Ladders, player starts from 1st cell and climbs up based on the number he gets on the roll of a dice. If the player encounters a ladder, he climbs up to the end of ladder. If a snake is encountered, the player has to come down to the cell where the snake ends.

Q1 - What is the distribution of nuber of turns required to complete the game.

Q2 - What is the probability of a game to be completed in 'x' turns.
Based on the board in image 

![](https://github.com/rohit-a/data-science-python/blob/master/01%20-%20Snakes%20and%20Ladders/IMG-01-Snakes_and_ladders_board.jpg)

### Game Rules:
 1. Player starts at cell 1 and throws a dice on each turn.
 2. Player moves up the number he gets on the dice.
 3. If the player encounters a ladder, he climbs up the ladder.
 4. If player encounters a snake, he has to come down to the end of the snake.
 5. Getting a 6 allows palyer to roll the dice again and move total number of both the rolls.
 6. The player completes a game when he reaches cell 100.
 7. Maximum number of turns a player gets is 1000.
 
 ##### Distribution of Moved to complete 5000 games
 
 ![](https://github.com/rohit-a/data-science-python/blob/master/01%20-%20Snakes%20and%20Ladders/VIZ-01-Distribution_of_Moves_to_Complete_Game.png)
 
 ##### Probability distribution of completing a game in X moves
 
 ![](https://github.com/rohit-a/data-science-python/blob/master/01%20-%20Snakes%20and%20Ladders/VIZ-02-Probability_of_Game_Completion.png)
 
