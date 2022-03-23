from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("yellow")
        self.setpos(0, 270)
        self.refresh()

    def increase(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.refresh()
