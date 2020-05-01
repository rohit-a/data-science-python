# Climbing Up Burj Khalifa - A Dice Roll Game

Player starts a game of climbing Burj Khalifa based on the number he gets on the roll of a dice. We would like to simulate 
several such climbs, each climb comprising of 100 turns to find out what is the final floor reached in each climb.

Q1 - What is the distribution of floor reached over 5000 walks.

Q2 - What is the probability distribution of reaching a floor over 100 turns.

Based on the problem in [Data Camp - Hacker Statistics Problem](https://campus.datacamp.com/courses/intermediate-python/case-study-hacker-statistics?ex=5)

### Game Rules:
 1. Player starts at floor 0 and throws a dice on each turn.
 2. If he gets 1,2 - player has to come down 1 floor.
 3. If he gets 3,4,5 - player climbs 1 floor.
 4. If he gets 6, he gets to throw 1 more time and climbs as many floors as the number in the throw.
 5. Clumsiness: 0.1% of time player trips and falls to Floor 0 (Without damage :D)
 6. By default, player gets to take 100 steps (throws dice 100 times)
    
 ##### Distribution of floor reached over 5000 walks
 
 ![](https://github.com/rohit-a/data-science-python/blob/master/00%20-%20Climbing%20Up%20Burj%20Khalifa/VIZ-02-Distribution_of_Floor_Reached.png)
 
 ##### Probability distribution of reaching a floor over 100 steps
 
 ![](https://github.com/rohit-a/data-science-python/blob/master/00%20-%20Climbing%20Up%20Burj%20Khalifa/VIZ-03-Probability_Distribution_of_Floor_Reached.png)
 
