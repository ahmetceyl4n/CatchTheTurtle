import turtle
import random

# Ekranı ayarla
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial',30, 'normal' )
score = 0
game_over = False

#turtle list
turtle_list = []

#score turtle

score_turtle = turtle.Turtle()

#countdown turtle

countdown_turtle = turtle.Turtle()

#properties
grid_size = 11
x_cordinates=[-20,-10,0,10,20]
y_cordinates=[-20,-10,0,10,20]


def setup_score_turtle():
    score_turtle.color("dark blue")

    top_hight = screen.window_height() /2
    y = top_hight * 0.8

    score_turtle.speed(0)
    score_turtle.penup()
    score_turtle.setposition(0,y)
    score_turtle.pendown()

    score_turtle.write(arg="Score : 0",move=False, align="center",font=FONT)
    score_turtle.hideturtle()




def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_cilck(x,y):
        global score
        score +=1
        score_turtle.clear()
        score_turtle.write(arg="Score : {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_cilck)

    t.penup()

    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)




def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)


def countdown(time):
    score_turtle.color("dark blue")

    top_hight = screen.window_height() / 2
    y = top_hight * 0.65
    countdown_turtle.hideturtle()
    countdown_turtle.speed(0)
    countdown_turtle.penup()
    countdown_turtle.setposition(0, y)
    countdown_turtle.pendown()
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time = {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
         global game_over
         game_over=True
         countdown_turtle.clear()
         hide_turtles()
         countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)



def start_game():

    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)



start_game()
turtle.mainloop()
