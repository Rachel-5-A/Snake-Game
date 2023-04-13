from turtle import Turtle, Screen

s = Screen()

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
INITIAL_POSITION = (0, 270)
CENTER = (0, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.goto(*INITIAL_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard to display the current score and high score"""
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1 and updates the scoreboard"""
        self.score += 1
        self.update_scoreboard()

    def increase_high_score(self):
        """ If the current score is higher than the high score, updates the high score
                and saves it to a file. Then updates the scoreboard"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_scoreboard()
            self.save_high_score()

    def reset_score(self):
        """Resets the score to 0 and updates the scoreboard"""
        self.score = 0
        self.update_scoreboard()
        self.goto(*INITIAL_POSITION)

    @staticmethod
    def load_high_score():
        # TODO: Implement loading the high score from a file or database
        return 0

    def save_high_score(self):
        # TODO: Implement saving the high score to a file or database
        pass
