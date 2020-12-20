from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x, y + self.y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self, option):
        self.x *= -1
        if option:
            self.move_speed *= 0.9
        else:
            self.move_speed = 0.1
