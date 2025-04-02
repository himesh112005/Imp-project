import turtle
import random
import time

def draw_balloon(x, y, color):
    balloon = turtle.Turtle()
    balloon.speed(5)
    balloon.penup()
    balloon.goto(x, y)
    balloon.pendown()
    balloon.color(color)
    balloon.begin_fill()
    balloon.circle(25)
    balloon.end_fill()
    balloon.hideturtle()

def draw_string(x, y):
    string = turtle.Turtle()
    string.speed(5)
    string.penup()
    string.goto(x, y)
    string.pendown()
    string.pensize(2)
    string.color("black")
    string.goto(x, y - 50)
    string.hideturtle()

def write_text(text, x, y, color, size, font="Comic Sans MS"):
    writer = turtle.Turtle()
    writer.speed(5)
    writer.penup()
    writer.goto(x, y)
    writer.pendown()
    writer.color(color)
    writer.write(text, font=(font, size, "bold"))
    writer.hideturtle()

def confetti():
    confetti_turtle = turtle.Turtle()
    confetti_turtle.speed(0)
    confetti_turtle.hideturtle()
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
    for _ in range(100):
        x = random.randint(-250, 250)
        y = random.randint(-150, 200)
        confetti_turtle.penup()
        confetti_turtle.goto(x, y)
        confetti_turtle.pendown()
        confetti_turtle.dot(random.randint(5, 10), random.choice(colors))

def draw_cake():
    cake = turtle.Turtle()
    cake.speed(5)
    cake.penup()
    cake.goto(-50, -50)
    cake.pendown()
    cake.color("brown")
    cake.begin_fill()
    for _ in range(2):
        cake.forward(100)
        cake.right(90)
        cake.forward(50)
        cake.right(90)
    cake.end_fill()
    cake.penup()
    cake.goto(-40, 0)
    cake.pendown()
    cake.color("white")
    cake.begin_fill()
    for _ in range(2):
        cake.forward(80)
        cake.right(90)
        cake.forward(30)
        cake.right(90)
    cake.end_fill()
    cake.hideturtle()

def draw_candles():
    candle = turtle.Turtle()
    candle.speed(5)
    candle.penup()
    candle.goto(-30, 5)
    candle.pendown()
    candle.color("red")
    candle.begin_fill()
    for _ in range(2):
        candle.forward(10)
        candle.right(90)
        candle.forward(20)
        candle.right(90)
    candle.end_fill()
    candle.penup()
    candle.goto(20, 5)
    candle.pendown()
    candle.begin_fill()
    for _ in range(2):
        candle.forward(10)
        candle.right(90)
        candle.forward(20)
        candle.right(90)
    candle.end_fill()
    candle.hideturtle()

def draw_flames():
    flame = turtle.Turtle()
    flame.speed(5)
    flame.penup()
    flame.goto(-25, 25)
    flame.pendown()
    flame.color("orange")
    flame.begin_fill()
    flame.circle(5)
    flame.end_fill()
    flame.penup()
    flame.goto(25, 25)
    flame.pendown()
    flame.begin_fill()
    flame.circle(5)
    flame.end_fill()
    flame.hideturtle()

# Setup the screen
turtle.bgcolor("lightblue")

# Write "Happy Birthday Unnati"
write_text("Happy", -180, 80, "red", 50)
time.sleep(0.5)
write_text("Birthday", -40, 80, "blue", 50)
time.sleep(0.5)
write_text("Unnati!", 50, 20, "purple", 50)
time.sleep(0.5)

# Draw balloons with strings
draw_balloon(-180, 120, "red")
draw_string(-180, 120)
draw_balloon(180, 120, "blue")
draw_string(180, 120)
draw_balloon(0, 150, "yellow")
draw_string(0, 150)

draw_balloon(-100, 140, "green")
draw_string(-100, 140)
draw_balloon(100, 140, "purple")
draw_string(100, 140)

# Draw cake and candles
draw_cake()
draw_candles()
draw_flames()

# Create confetti animation
confetti()

# Keep the window open
turtle.done()
