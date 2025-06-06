import turtle

bob = turtle.Turtle();
bob.shape("turtle")
bob.color("blue")
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.right(90)
bob.backward(50)
bob.circle(50)
bob.penup()
bob.goto(0, 0)
bob.pendown()
bob.write("Hello, Turtle!", font=("Arial", 16, "normal"))
turtle.done()
