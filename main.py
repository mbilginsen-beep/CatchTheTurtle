import turtle
import random


drawing_board= turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch the Turtle")

turtle_ins=turtle.Turtle()
turtle_ins.shape("turtle")
turtle_ins.color("green")
turtle_ins.shapesize(2)

timer_turtle=turtle.Turtle()
timer_turtle.color("red")
timer_turtle.hideturtle()
timer_turtle.teleport(0,500)

score_turtle=turtle.Turtle()
score_turtle.color("black")
score_turtle.hideturtle()
score_turtle.teleport(0, 470)

#counter=int(input("Enter how many seconds you want to play: "))

counter=10
score=0

def my_function(x,y):
    global score
    score += 1

def move_turtle():
    global counter
    timer_turtle.clear()
    score_turtle.clear()
    timer_turtle.write(f"Time: {counter}",align="center", font=("Arial", 24, "normal"))
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    x = random.randint(-960, +960)
    y = random.randint(-540, +540)
    turtle_ins.teleport(x, y)
    counter -= 1
    turtle_ins.onclick(my_function)

    # Set timer for 1000ms (1 second) and recall countdown
    if counter >= 0:
        drawing_board.ontimer(move_turtle,1000)

    if counter < 0:
        timer_turtle.clear()
        timer_turtle.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
        turtle_ins.hideturtle()

move_turtle()

turtle.mainloop()