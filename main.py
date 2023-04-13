from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up constants for readability
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FOOD_DISTANCE_THRESHOLD = 15
WALL_DISTANCE_THRESHOLD = 280
TAIL_DISTANCE_THRESHOLD = 10

# Set up the screen, snake, food, and scoreboard
s = Screen()
s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def set_key_listeners():
    """Set up the key listeners for controlling the snake"""
    s.listen()
    s.onkey(snake.up, "Up")
    s.onkey(snake.down, "Down")
    s.onkey(snake.left, "Left")
    s.onkey(snake.right, "Right")


def reset_game():
    """Reset the game objects to their initial state"""
    food.refresh()
    snake.snake_reset()
    scoreboard.reset_score()
    scoreboard.update_scoreboard()
    set_key_listeners()


def check_collision():
    """Check for collisions with food, walls, and tail segments"""
    if snake.head.distance(food) < FOOD_DISTANCE_THRESHOLD:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.increase_high_score()

    if (
        snake.head.xcor() > WALL_DISTANCE_THRESHOLD or
        snake.head.xcor() < -WALL_DISTANCE_THRESHOLD or
        snake.head.ycor() > WALL_DISTANCE_THRESHOLD or
        snake.head.ycor() < -WALL_DISTANCE_THRESHOLD
    ):
        return True

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < TAIL_DISTANCE_THRESHOLD:
            return True

    return False


def move_snake():
    """Move the snake and update the screen"""
    s.update()
    time.sleep(0.1)
    if game_is_on:  # only move the snake if the game is on
        snake.move()


# Start the game loop
game_is_on = True
while game_is_on:
    set_key_listeners()
    move_snake()

    if check_collision():
        game_is_on = False
        # Ask the player if they want to play again
        play_again = s.textinput("Game Over", "Do you want to play again? (y/n)")
        if play_again == 'y':
            game_is_on = True
            reset_game()
        else:
            s.bye()
