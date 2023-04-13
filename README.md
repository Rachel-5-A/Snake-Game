# Snake game

This is a simple version of the classic Snake game, built using Python and the Turtle graphics library. The goal of the game is to navigate the snake around the screen and eat as many pieces of food as possible without colliding with the walls or the snake's own tail.

## Getting Started

To play the game, simply run the **'main.py'** file using Python 3. Make sure that you have the turtle module installed. If you don't have it installed, you can install it using the following command:

```python
pip install turtle
```

### How to Play

* Use the arrow keys to control the direction of the snake

* Eat the pieces of food to score points

* Avoid colliding with the walls or the snake's own tail

* The game ends when the snake collides with a wall or its own tail

## Code overview

The code is split into several files:

* **'main.py':**
This file contains the main game loop, which runs continuously until the game is over. It also initializes the other game objects (the snake, food, and scoreboard) and handles user input.

* **'snake.py':** 
This file contains the **'Snake'** class, which represents the snake in the game. The **'Snake'** class has several methods for controlling the snake's movement and behavior, including **'move()'**, which moves the snake forward one step, and **'extend()'**, which adds a new segment to the end of the snake.

* **'food.py':** 
This file contains the **'Food'** class, which represents the pieces of food in the game. The **'Food'** class has a **'refresh()'** method, which moves the food to a random location on the screen and changes its color.

* **'scoreboard.py':** 
This file contains the **'Scoreboard'** class, which keeps track of the player's score and high score. The **'Scoreboard'** class has methods for increasing the score, resetting the score.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue.

## Credits 

This game was inspired by the Udemy course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Angela Yu. Feel free to use this code as a starting point for your own projects.
