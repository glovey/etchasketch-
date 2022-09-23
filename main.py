from random import randint
from random import choice
import turtle as t



tim = t.Turtle()
screen = t.Screen()
screen.listen()
screen.tracer(0)
tim.up()
tim.speed("slowest")



def forward():
  tim.forward(10)
  tim.setpos(tim.pos())  
  screen.update()

def backward():
  tim.backward(10)
  screen.update()

def right():
  tim.setheading(tim.heading() - 10)
  screen.update()
def left():
  tim.setheading(tim.heading() + 10)
  screen.update()
  
def pen_down():
  tim.down()
  
def pen_up():
  tim.up()

def clear():
  tim.clear()
  tim.up()
  tim.home()

def c_bomb():
  tim.write("Crisps",False,"left",("Arial",8,"normal"))
  screen.update()

screen.onkeypress(forward,"Up")
screen.onkeypress(backward,"Down")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")
screen.onkeypress(pen_down,"a")
screen.onkeyrelease(pen_up,"a")
screen.onkeypress(c_bomb,"d")
screen.onkey(clear,"c")








  






screen.exitonclick()

