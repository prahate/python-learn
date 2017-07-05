import turtle

def draw_polygon(some_turtle):
	some_turtle.left(120)
	some_turtle.forward(100)
	some_turtle.right(60)
	some_turtle.forward(100)
	some_turtle.right(120)
	some_turtle.forward(100)
	some_turtle.right(60)
	some_turtle.forward(100)


def draw_flower():
	window = turtle.Screen()
	window.bgcolor("yellow")

	brad = turtle.Turtle()
	brad.color("red")
	brad.shape("turtle")
	#brad.speed(1)

	for i in range(72):
		draw_polygon(brad)
		brad.right(5)

	brad.right(90)
	brad.forward(300)

	window.exitonclick();

draw_flower()
