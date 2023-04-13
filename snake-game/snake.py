from turtle import Turtle, Screen

s = Screen()

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SEGMENT_SHAPE = "circle"
SEGMENT_COLOR = "green"
HEAD_COLOR = "DarkSlateGray"


class Snake:
    def __init__(self, body_color="green"):
        self.body_color = body_color
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.start_position = (0, 0)
        self.start_direction = RIGHT
        self.snake_reset()

    def create_snake(self):
        """Create the initial snake with three segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at the specified position"""
        new_segment = Turtle(shape=SEGMENT_SHAPE)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        if position == STARTING_POSITIONS[0]:
            new_segment.color(HEAD_COLOR)
        else:
            new_segment.color(self.body_color)

    def extend(self):
        """Add a new segment to the end of the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        s.update()

    def up(self):
        """Turn the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_reset(self):
        """Reset the snake to its initial state"""
        for segment in self.segments:
            segment.goto(1000, 1000)  # move segments off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.setheading(self.start_direction)
