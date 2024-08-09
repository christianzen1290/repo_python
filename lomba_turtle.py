from turtle import Turtle,Screen
import random
tim = Turtle()
screen = Screen()

is_race_on = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Enter a color")
colors = ['red','orange','yellow','green','blue','purple']
all_turtle = []

y_position = -100
for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_position)
    y_position = y_position +30
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True 

while is_race_on:
    

    for turtle in all_turtle:
        if(turtle.xcor() > 230):
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won")
            else:
                print(f"you lost. {winning_color} won")
            is_race_on = False
        rand_distance = random.randint(0,10)
        if(turtle.pencolor() == 'red'):
            rand_distance = random.randint(0,12)
        turtle.forward(rand_distance)


screen.exitonclick()