import random
from turtle import Turtle,Screen
import random
screen = Screen()

screen.setup(height=500,width=500)
user_guess = screen.textinput(title="Make your bet",prompt="Which turtle will win the game\n1.red\n2.orange\n3.yellow\n4.green\n5.blue\n6.purple")


directions = [-70,-40,-10,20,50,80]
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

for i in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=directions[i])
    all_turtles.append(new_turtle)

if user_guess:
    is_true = True


while is_true:
    for i in all_turtles:
        if i.xcor() >= 230 :
            is_true = False
            winning_color = i.pencolor()
            if user_guess == winning_color:
                print(f"{winning_color}, You win.")
            else:
                print(f"You lose,{winning_color} wins the race")
        i.forward(random.randint(0,10))


screen.exitonclick()
