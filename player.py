from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """
        Move player's turtle up.
        """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """
        Sends player's turtle to start.
        """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """
        Checks for level completed.
        :return: True/False whether turtle is at finish line.
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
