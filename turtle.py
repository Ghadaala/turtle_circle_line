import turtle
from turtle import Screen, Turtle, mainloop


def inforGneral():
        wn = turtle.Screen()
        turtle.bgcolor("black")
        turtle.pensize(2)
        turtle.speed(0)



def theMainCircle():
        for i in range(6):
                for colors in ["pink", "cyan", "purple", "red", "yellow", "orange"]:
                        turtle.color(colors)
                        turtle.circle(100)
                        turtle.left(10)
def t1():
        turtle.clone()
        turtle.setpos(-150,170)
        turtle.penup()

def slope(x1, y1, x2, y2):
        if(x2 - x1 != 0):
                turtle.pensize(3)
                turtle.pencolor(orange)
                return abs((float)(y2-y1)/(x2-x1))
        
        turtle.pendown()

def secondC():
        for i in range(6):
                for colors in ["pink", "cyan", "purple", "red", "yellow", "orange"]:
                        turtle.color(colors)
                        turtle.circle(15)
                        turtle.left(10)
def t2():
        turtle.clone()
        turtle.setpos(150,-170)
        turtle.rt(300.0)
        turtle.penup()

def slope(x1, y1, x2, y2):
        if(x2 - x1 == 0):
                turtle.pensize(3)
                turtle.pencolor(orange)
                return abs((float)(y2-y1)/(x2-x1))
        
        turtle.pendown()
        
def thirdC():
        for i in range(6):
                for colors in ["pink", "cyan", "purple", "red", "yellow", "orange"]:
                        turtle.color(colors)
                        turtle.circle(15)
                        turtle.left(10)
def main():
        inforGneral()
        theMainCircle()
        t1()
        slope( x1 = -110,y1 =200, x2=200, y2=-110)
        secondC()
        t2()
        slope(x1=110, y1=-200, x2=200, y2=-110)
        thirdC()
        
        
        
main()       
        



     
        

turtle.hideturtle()       
turtle.mainloop()            



