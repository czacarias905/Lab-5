#Cecilia Zacarias
#2/13/2020

#This program asks the user for a number of sides, length of sides, color of lines, and fill in color of a regular polygon.

import turtle
ceci = turtle.Turtle()

sides = int(input ("Number of sides in polygon?"))
length = int (input ("What length would you like the sides?"))
lcolor = input("What color do you want your sides?")
fcolor = input("What color do you want for the inside?")

ceci = turtle.Turtle()

ceci.color(str(lcolor))
ceci.fillcolor(str(fcolor))
ceci.begin_fill()
#ceci.end_fill()
ceci.pencolor(str(lcolor))

for i in range(sides):
    #ceci.pencolor = (str(lcolor))
    #ceci.fillcolor = (str(fcolor))
    ceci.forward(length)
    ceci.left(360 / sides)

ceci.color = (lcolor)
ceci.fillcolor = (fcolor)
ceci.end_fill()
