import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Desactiva las actualizaciones automáticas de la pantalla

# Marcador
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.shape("square")
score_turtle.color("white")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)
score_turtle.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Comida de la serpiente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Funciones
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Función para mostrar mensaje de pérdida
def show_message(message):
    message_turtle = turtle.Turtle()
    message_turtle.speed(0)
    message_turtle.shape("square")
    message_turtle.color("red")
    message_turtle.penup()
    message_turtle.hideturtle()
    message_turtle.goto(0, 0)
    message_turtle.write(message, align="center", font=("Courier", 24, "normal"))
    time.sleep(2)
    message_turtle.clear()

# Teclado
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Función para actualizar el marcador
def update_score():
    score_turtle.clear()
    score_turtle.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Bucle principal del juego
while True:
    wn.update()

    # Colisiones con el borde (vuelta a la pantalla)
    if head.xcor() > 290:
        head.setx(-290)
    elif head.xcor() < -290:
        head.setx(290)
    elif head.ycor() > 290:
        head.sety(-290)
    elif head.ycor() < -290:
        head.sety(290)

    # Colisiones con la comida
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Aumenta la puntuación
        score += 10

        if score > high_score:
            high_score = score

        # Actualiza el marcador
        update_score()

        # Acelera el juego
        delay -= 0.001

    # Mueve el cuerpo de la serpiente
    total_segments = len(segments)
    for index in range(total_segments - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if total_segments > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Colisiones con el cuerpo
    for segment in segments[1:]:  # Comienza desde el segundo segmento
        if head.distance(segment) < 20:
            show_message("¡Te comiste!")
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Oculta los segmentos
            for segment in segments:
                segment.goto(1000, 1000)

            # Limpia la lista de segmentos
            segments.clear()

            # Resetea la puntuación y el retraso
            score = 0
            update_score()
            delay = 0.1

    time.sleep(delay)

wn.mainloop()
