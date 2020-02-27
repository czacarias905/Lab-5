#Cecilia Zacarias
#2/16/2020

# This program is an attempt to draw a flower with Turtle methods.

import turtle

#Create Window
window = turtle.Screen()
fleur = turtle.Turtle()

#Draw Stem and Circle
fleur.color("green", "black")
fleur.left(90)
fleur.forward(100)
fleur.right(90)

fleur.color("dark orange", "orange")
fleur.begin_fill()
fleur.circle(10)
fleur.end_fill()

#Draw all petals
for i in range(1, 24):
    
    if fleur.color() == ("red", "black"):
        fleur.color("cyan", "black")
    
    elif fleur.color() == ("cyan", "black"):
        fleur.color("pink", "black")
    
    else:
        fleur.color("red", "black")

    fleur.left(15)
    fleur.forward(50)
    fleur.left(157)
    fleur.forward(50)

#Hide that turtle
fleur.hideturtle()

#Tidy up Window
window.exitonclick()


