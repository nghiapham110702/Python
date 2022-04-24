# Nghia Pham
# ngmpham
# programming assigment 2
# This program will use turtle module and for loop to draw a polygon at the center and then use for loop
# to draw multiple triangle around polygon to form a star with filled color green in it.
# Each triangle will have red dot at the top and will draw as many side depend on the user input which must be
# odd number and greater than 3
import turtle

n = int(input('Enter an odd greater than or equal to 3: '))
wn = turtle.Screen()
wn.title(str(n)+"-pointed star")

John = turtle.Turtle()
John.color("blue", "green")  # pen color, fill color
John.pensize(2)

John.penup() # so the turtle will not draw anything while moving to position (-150, 0)
John.setpos(-150, 0)
John.pendown() # Start drawing
angle = 180/n
rotation = 180-angle# rotation of the angle need it
John.begin_fill()
for i in range(n):
    John.forward(300)# form the polygon depend the side of user input
    John.right(rotation)
    # end for loop 1
John.end_fill()
John.color("red")
for i in range(n):
    John.penup()
    John.forward(300) # drawing the trianlte that will form the star
    John.pendown()
    John.begin_fill()
    John.dot(10)
    John.end_fill()
    John.right(rotation)
    #end for loop2
wn.mainloop()