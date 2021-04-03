from turtle import Turtle
DIRECTIONS = {'UP': 90,
              'DOWN': 270,
              'LEFT': 180,
              'RIGHT': 0}

class Slug:
    def __init__(self):
        self.body = []

    def start_body(self, length):
        for num in range(0, length):
            body_part = Turtle()
            body_part.shape("square")
            body_part.color("white")
            body_part.goto(-20 * num, 0)
            self.body.append(body_part)

    def add_body(self):
        body_part = Turtle()
        body_part.shape("square")
        body_part.color("white")
        body_part.penup()
        self.body.append(body_part)



    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            self.body[part].goto(new_x, new_y)
        self.body[0].forward(20)

    def up(self):
        # self.body[0].goto(self.body[0].xcor(), self.body[0].ycor() + 20)
        if self.body[0].heading() != DIRECTIONS['DOWN']:
            self.body[0].setheading(DIRECTIONS['UP'])

    def down(self):
        # self.body[0].goto(self.body[0].xcor(), self.body[0].ycor() - 20)
        if self.body[0].heading() != DIRECTIONS['UP']:
            self.body[0].setheading(DIRECTIONS['DOWN'])

    def left(self):
        # self.body[0].goto(self.body[0].xcor() - 20, self.body[0].ycor())
        if self.body[0].heading() != DIRECTIONS['RIGHT']:
            self.body[0].setheading(DIRECTIONS['LEFT'])

    def right(self):
        # self.body[0].goto(self.body[0].xcor() + 20, self.body[0].ycor())
        if self.body[0].heading() != DIRECTIONS['LEFT']:
            self.body[0].setheading(DIRECTIONS['RIGHT'])
