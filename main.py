import turtle
import random
import time

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

time_sec=0
score=0
gameover=False
game_pl=False

def time_turtle():
    global time_sec
    global game_pl
    time_turtle = turtle.Turtle()
    time_turtle.color("dark blue")
    time_turtle.hideturtle()
    time_turtle.teleport(0,30)
    # Using .numinput function no need for the lines 41, 42 and 44 anymore but that's another way of getting and showing the time input
    '''time_turtle.write("Enter how many seconds you want to play & press enter: ",
                      align="center", font=("Arial", 24, "normal"))'''
    time_sec=int(drawing_board.numinput("SET TIME", "Enter how many seconds you want to play:"))
    #time_sec= int(input("Enter how many seconds you want to play: "))
    if time_sec > 0:
        time_turtle.clear()
        time_turtle.write(f"PLAY FOR {time_sec} SECONDS. HAVE FUN!",
                      align="center", font=("Arial", 24, "normal"))
        time.sleep(2)
        time_turtle.clear()
        game_pl = True

def my_function(x,y):
    global score
    score += 1

def countdown(time_sec):
    global gameover
    timer_turtle.clear()
    timer_turtle.write(f"Time: {time_sec}", align="center", font=("Arial", 24, "normal"))
    if time_sec > 0:
        drawing_board.ontimer(lambda: countdown(time_sec-1),1000)
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
    if not gameover:
        drawing_board.ontimer(move_turtle,1250) # One may increase of decrease the speed of the turtle by tuning the time in miliseconds
    else:
        score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

time_turtle()

if game_pl:
    countdown(time_sec)
    move_turtle()

turtle.mainloop()