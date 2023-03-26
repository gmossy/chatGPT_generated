# Ping-Pong This is a basic code structure for a ping pong game written in Python.Feel free to customize and add your
# own functionalities to the game.
import turtle
# from turtle import *

# Step2: Setup screen

screen = turtle.Screen()

screen.title("Ping Pong Game")

screen.bgcolor("black")

screen.setup(width=600, height=400)

# Step3: Create the paddles

paddle_a = turtle.Turtle()

paddle_a.speed(0)

paddle_a.shape("square")

paddle_a.color("white")

paddle_a.shapesize(stretch_wid=6, stretch_len=1)

paddle_a.penup()

paddle_a.goto(-250, 0)

paddle_b = turtle.Turtle()

paddle_b.speed(0)

paddle_b.shape("square")

paddle_b.color("white")

paddle_b.shapesize(stretch_wid=6, stretch_len=1)

paddle_b.penup()

paddle_b.goto(250, 0)

# Step 4: Create the ball

ball = turtle.Turtle()

ball.speed(40)

ball.shape("circle")

ball.color("white")

ball.penup()

ball.goto(0, 0)

ball.dx = 0.5

ball.dy = 0.5

# Step 5: Create the score system

score_a = 0

score_b = 0

score = turtle.Turtle()

score.speed(0)

score.color("white")

score.penup()

score.hideturtle()

score.goto(0, 180)

score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Step 6: Create the movement of the paddles

def paddle_a_up():
    y = paddle_a.ycor()

    y += 20

    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()

    y -= 20

    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()

    y += 20

    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()

    y -= 20

    paddle_b.sety(y)


screen.listen()

screen.onkeypress(paddle_a_up, "w")

screen.onkeypress(paddle_a_down, "s")

screen.onkeypress(paddle_b_up, "Up")

screen.onkeypress(paddle_b_down, "Down")

# Step 7: Create the main game loop

while True:

    screen.update()

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 190:
        ball.sety(190)

        ball.dy *= -1

    if ball.ycor() < -190:
        ball.sety(-190)

        ball.dy *= -1

    if ball.xcor() > 290:
        ball.goto(0, 0)

        ball.dy *= -1

        score_a += 1

        score.clear()

        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                    font=("Courier", 24, "normal"))

    if ball.xcor() < -290:
        ball.goto(0, 0)

        ball.dy *= -1

        score_b += 1

        score.clear()

        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                    font=("Courier", 24, "normal"))

    if (240 < ball.xcor() < 250) and (
            paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(240)

        ball.dx *= -1

    if (-240 > ball.xcor() > -250) and (
            paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-240)

        ball.dx *= -1
