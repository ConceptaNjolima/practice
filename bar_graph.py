#####
# Name: Concepta Njolima
# Username:njolimac
#
#
# This is my own coding time where I get to try ou new things: And today, I get to draw a Bar graph.
##Thinking of appplying it to data science
#######

import turtle


def draw_frame(turtle):
    """
    This function draws the border framefor the graph

    :param turtle: Name of the turtle
    :return: none
    """
    turtle.penup()
    turtle.setpos(-200, 200)
    turtle.pendown()
    turtle.color("blue")
    turtle.left(-90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.penup()


def draw_bar(turtle, data):
    """
    This function is for drawing the bars of the graph
    :param turtle: Takes the name of the turtle
           data: This provides the data set to be evaluated.
    :return: None
    """
    turtle.setpos(-200, -200)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):

        turtle.color("green", "orange")
        turtle.left(90)
        turtle.forward(data[i] * 5)
        turtle.left(-90)
        turtle.forward(50)
        turtle.write(data[i])
        turtle.left(-90)
        turtle.forward(data[i] * 5)
        turtle.left(90)
    turtle.end_fill()

def main():
    """This is the main function.Where everything begins!"""
    wn = turtle.Screen()
    wn.bgcolor("pink")
    pencil = turtle.Turtle()
    data = [20, 30, 40, 20, 5,27]
    draw_frame(pencil)
    draw_bar(pencil, data)

    wn.exitonclick()


main()
