from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Re-write updated data to scoreboard to be seen.
        """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """
        Increase level of player on scoreboard, and updates scoreboard to
        display change.
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
         Send player to start, and display GAME OVER.
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
