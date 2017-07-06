import turtle

def write_name(name):
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.color("yellow")
	brad.write(name, font=("Aerial", 30))
	
	window.exitonclick()

write_name("Prathamesh")
