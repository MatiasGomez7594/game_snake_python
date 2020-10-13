import turtle
import time
import random

posponer = 0.1

#marcador puntaje
score = 0
high_score = 0

#ventana del juego
ventana = turtle.Screen()
ventana.title("Game Snake")
ventana.bgcolor("black")
ventana.setup(width=600,height=600)
ventana.tracer(0)


#cabeza de la serpiente, el tamaño de la serpiente por defecto es 20px
cabeza = turtle.Turtle()
cabeza.color("green")
cabeza.speed(0)
cabeza.shape("square")
#quita el rastro de la serpiente
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"

#comida de la serpiente
comida = turtle.Turtle()
comida.color("red")
comida.speed(0)
comida.shape("circle")
#quita el rastro de la serpiente
comida.penup()
comida.goto(0,0)
comida.direction="stop"

#cuerpo de la serpiente
segmentos = []

#puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0        High Score:0",   align="center", font=("courier",24,"normal"))
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def izquierda():
    cabeza.direction = 'left'
def derecha():
    cabeza.direction = 'right'
#funciones de movimiento

def movimientos():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y+20)
        
    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y-20)
        
    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x-20)
        
    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x+20)
        
#control teclado
ventana.listen()
ventana.onkeypress(arriba,'Up')
ventana.onkeypress(abajo,'Down')
ventana.onkeypress(izquierda,'Left')
ventana.onkeypress(derecha,'Right')
#bucle para que funcione el juego 
while True:
    ventana.update()
    #colisiones bordes, para perder
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor()> 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #cuando se pierde vuelve el puntaje a 0
        score = 0
        texto.clear()
        texto.write("Score:{}       High Score:{}".format(score,high_score),align="center", font=("courier",24,"normal"))
   
        for segmento in segmentos:
            segmento.hideturtle()
        segmentos.clear()

    #chequeo la distancia entre la serpiente y la comida
    if cabeza.distance(comida)<20:
        #asi muevo la comida por la ventana
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        
        #asi incremento el tamaño de la serpiente
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.color("green")
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #aumentar marcador
        score +=10
        texto.clear()
        texto.write("Score:{}       High Score:{}".format(score,high_score),align="center", font=("courier",24,"normal"))

        if score > high_score:
            high_score = score
            
            #para actualizar el puntaje a medida que jugamos
            texto.clear()
            #texto.color("white")
            #texto.penup()
            #texto.hideturtle()
            #texto.goto(0,260)
            texto.write("Score:{}       High Score:{}".format(score,high_score),align="center", font=("courier",24,"normal"))
            

        

    total_segmentos = len(segmentos)
    #para mover el cuerpo de la serpiente
    for index in range(total_segmentos-1,0,-1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x,y)
        
    if total_segmentos >0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
        
    movimientos()

    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"
            score = 0
            texto.clear()
            texto.write("Score:{}       High Score:{}".format(score,high_score),align="center", font=("courier",24,"normal"))
            for segmento in segmentos:
                segmento.hideturtle()
            segmentos.clear()

    
    time.sleep(posponer)
    


#for i in range(0,4):
 #   pluma.left(90)
  #  pluma.forward(100)
