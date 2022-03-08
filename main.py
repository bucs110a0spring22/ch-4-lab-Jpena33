import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def setupWindow(mywindow=None):
  sc = turtle.Screen()
  fred = turtle.Turtle()  
  sc.setworldcoordinates(-360,-1,360,1)
  fred.speed(20)
  fred.goto(-360,0)
  fred.goto(360,0)

def setupAxis(fred=None):
  fred.goto(0,0)
  fred.goto(0,1)
  fred.goto(0,-1)

def drawSineCurve(fred=None):
  fred.penup()
  fred.goto(-360,0)
  fred.pendown()
for sinx in range(-360,361):
  fred = turtle.Turtle()
  siny = math.sin(math.radians(90))
  fred.goto(90,180)
  fred.goto(150,160)
  print (90,180)
  print(150,160)
sin()

def drawCosineCurve(fred=None):
  fred.penup()
  fred.goto(-360,0)
  fred.pendown()
  fred.pencolor('red')
for cosx in range(-360,361):
  cosy = math.cos(math.radians(90))
  fred.goto(90,180)
  print (90,180)
cos()

def drawTangentCurve(fred=None):
  fred.penup()
  fred.pencolor('blue')
  fred.goto(-360,0)
  fred.pendown()
for tanx in range(-360,361):
  tany = math.tan(math.radians(tanx))
if tany <= 1 :
  fred.pendown()
fred.goto(tanx,tany)
if tany >= -1 :
  fred.pendown()
  fred.goto(tanx,tany)
else:
  fred.penup()
  fred.goto(tanx,-1)
  print(tanx,tany)
tan()



##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
