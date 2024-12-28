import turtle
import random

colors = ["grey", "chartreuse4", "teal", "DarkOrchid4", "darkgoldenrod4", "chocolate", "MidnightBlue", "peachpuff4"]

# Draw a rectangle (grid or Gotian pieces)
def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Draw the gotians (player pieces)
def draw_goat(t,game,a, b):
    for i in range(a, b):
        if game[2][i] != "":
            col = random.choice(colors)
            draw_rectangle(t, game[0][i][0], game[0][i][1], 40, 40, col)
            t.penup()
            t.goto(game[1][i][0], game[1][i][1])
            t.pendown()
            t.write(game[2][i], font=("modern love", 15, "bold"))
