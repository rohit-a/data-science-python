# Snakes and Ladders

In a classic game of Snake and Ladders, player starts from 1st cell and climbs up based on the number he gets on the roll of a dice. If the player encounters a ladder, he climbs up to the end of ladder. If a snake is encountered, the player has to come down to the cell where the snake ends.

Q1 - What is the distribution of nuber of turns required to complete the game.

Q2 - What is the probability distribution of compelting the game in 'x' turns.

Q3 - What is the distribution of Snakes or Ladders encountered for completed games.

Based on the board in image 

![](https://github.com/rohit-a/data-science-python/blob/master/00%20-%20Climbing%20Up%20Burj%20Khalifa/VIZ-02-Distribution_of_Floor_Reached.png)

### Game Rules:
 1. Player starts at cell 1 and throws a dice on each turn.
 2. Player moves up the number he gets on the dice.
 3. If the player encounters a ladder, he climbs up the ladded.
 4. If player encounters a snake, he has to come down to the end of the snake.
 5. Getting a 6 allows palyer to roll the dice again and move total number of both the rolls.
 6. The player completes a game when he reaches cell 100.