import turtle

def draw_square(some_turtle):
	for i in range(4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")

	for i in range(72):
		draw_square(brad)
		brad.right(5)
	
	#brad1 = turtle.Turtle()
	#brad1.shape("classic")
	#brad1.color("blue")
	#brad1.circle(100)

	window.exitonclick()

draw_art()
