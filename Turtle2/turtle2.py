from turtle import Turtle, Screen
import random

colours = ["green","red","blue"]

def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for _ in range(number_of_sides):
        tim.color(random.choice(colours))
        tim.forward(60)
        tim.right(angle)

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for item in range(3,10):
    draw_shape(item)

screen = Screen()
screen.exitonclick()