import turtle as t
import random as rd

t.bgcolor('yellow')
caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.hideturtle()
caterpillar.penup()

leaf=t.Turtle()
leaf_shape=((0,0),(5,15),(10,18),(20,20),(18,10),(15,5))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.speed(0)
leaf.penup()

game_on=False

score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.penup()

text=t.Turtle()
text.write('Press SPACE to start',align='center',font=('arial',16,'bold'))
text.hideturtle()

def isoutside():
    (x,y)=caterpillar.pos()
    right_wall=t.window_width()/2
    left_wall=-t.window_width()/2
    top_wall=t.window_height()/2
    bottom_wall=-t.window_height()/2
    outside=x>right_wall or x<left_wall or y>top_wall or y<bottom_wall
    return outside

def place_leaf():
    limx=t.window_width()/2-50
    limy=t.window_height()/2-50

    x=rd.randint(-limx,limx)
    y=rd.randint(-limy,limy)
    leaf.goto(x,y)

def disp_score(cur_score):
    score_turtle.clear()
    x=t.window_width()/2-50
    y=t.window_height()/2-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(cur_score),align='right',font=('arial',16))

def game_over():
    leaf.color('yellow')
    caterpillar.color('yellow')
    text.write("GAME OVER !",align='center',font=('arial',16,'bold'))

def start_game():
    global game_on
    if game_on:
        return;
    game_on=True
    cur_score=0
    text.hideturtle()
    text.clear()
    caterpillar_length=3
    caterpillar.shapesize(1,caterpillar_length,2)
    caterpillar_speed=2
    caterpillar.showturtle()
    place_leaf()
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)<20:
            place_leaf()
            cur_score+=1
            caterpillar_speed+=1
            disp_score(cur_score)
        if isoutside():
                game_over()
                break;


def move_up():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
        caterpillar.setheading(270)
def move_left():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(180)
def move_right():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(0)




t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_right,'Right')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
