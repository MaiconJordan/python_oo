import turtle

# Configurações iniciais
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.bgcolor("white")
t.pensize(20)
t.pencolor("black")

# Função para desenhar uma barra inclinada
def barra(x, y, altura, inclinacao):
    t.penup()
    t.goto(x, y)
    t.setheading(inclinacao)
    t.pendown()
    t.forward(altura)
    t.penup()

# Desenha as três barras
barra(-100, -50, 180, 75)
barra(-30, -50, 140, 75)
barra(30, -50, 100, 75)

turtle.done()