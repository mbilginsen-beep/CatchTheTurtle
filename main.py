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
#y=drawing_board.window_height() # küçük ekranda oynamak için kullanılabilir
#timer_turtle.teleport(0,y/2*0.9)
timer_turtle.teleport(0,510)

score_turtle=turtle.Turtle()
score_turtle.color("black")
score_turtle.hideturtle()
#score_turtle.teleport(0, y/2*0.8) # küçük ekran için kullanılabilir
score_turtle.teleport(0, 480)

#time=0
score=0
gameover=False

'''def time_turtle():
    global time
    time_turtle = turtle.Turtle()
    time_turtle.color("dark blue")
    time_turtle.hideturtle()
    time= int(input(time_turtle.write("Enter how many seconds you want to play: ", align="center", font=("Arial", 24, "normal"))))
    #timer_turtle.write(f"Enter how many seconds you want to play: {time}", align="center", font=("Arial", 24, "normal"))
    timer_turtle.clear()'''

def my_function(x,y):
    global score
    score += 1

def countdown(time):
    global gameover
    timer_turtle.clear()
    timer_turtle.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))
    if time > 0:
        drawing_board.ontimer(lambda: countdown(time-1),1000)
    else:
        timer_turtle.clear()
        timer_turtle.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        gameover=True
        turtle_ins.hideturtle()


def move_turtle():
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    x = random.randint(-960, +960)
    y = random.randint(-540, +540)
    turtle_ins.teleport(x, y)
    turtle_ins.onclick(my_function)

    # Set timer for 1000ms (1 second) and recall countdown
    if not gameover:
        #turtle_ins.clear()
        drawing_board.ontimer(move_turtle,1250)
    else:
        score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
        #turtle_ins.hideturtle()

'''time_turtle()

if time > 0:
    countdown(time)
    move_turtle()'''

countdown(10)
move_turtle()



turtle.mainloop()