from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def add_segment(self, position):
        segment = Turtle("square")
        segment.direction = 0
        segment.penup()
        segment.color("white")
        segment.setpos(position)
        self.snake.append(segment)

    def create_snake(self):
        for x in range(0, 3):
            self.add_segment((x * -MOVE_DISTANCE, 0))

    def move(self):
        for segment in range(len(self.snake)-1, 0, -1):
            self.snake[segment].setpos(self.snake[segment-1].pos())
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        self.add_segment(self.snake[-1].pos())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_wall_collision(self):
        return self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280

    def is_tail_collision(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def reset(self):
        for segment in self.snake:
            segment.setpos(999, 999)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
