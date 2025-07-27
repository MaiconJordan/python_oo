import turtle

# Cores dos anéis olímpicos
cores = ["blue", "black", "red", "yellow", "green"]

# Posições dos anéis (x, y)
posicoes = [(-120, 0), (0, 0), (120, 0), (-60, -50), (60, -50)]

# Cria a janela e a tartaruga
tela = turtle.Screen()
t = turtle.Turtle()
t.width(8)
t.speed(0)

# Desenha os cinco anéis
for cor, pos in zip(cores, posicoes):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.pencolor(cor)
    t.circle(60)

# Mantém a janela aberta até que seja fechada
tela.mainloop()