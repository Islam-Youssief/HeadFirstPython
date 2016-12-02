#Author : Islam Youssief Mohamed
import turtle
import random
window = turtle.Screen()
window.bgcolor("black")
abc =turtle.Turtle()
abc.shape("arrow")
abc.speed(2)

#for alphabet I
abc.pensize(5)
abc.color('red')
abc.fillcolor(1,1,0)
abc.pu()
abc.setx(-80)
abc.left(90)
abc.pd()
abc.fd(170)
abc.pu()
abc.fd(20)
abc.pd()
abc.dot(25,'red')
abc.pu()

#for alphabet S
abc.color("orange")
abc.setpos(0,100)
abc.pd()
abc.left(250)
abc.circle(50,-270)
abc.pu()
abc.setpos(0,100)
abc.pd()
abc.left(100)
abc.circle(50,-270)

#for alphabet L
abc.color("blue")
abc.pu()
abc.setpos(100,200)
abc.pd()
abc.left(180)
abc.bk(200)
abc.right(70)
abc.fd(50)

x = abc.xcor()
y = abc.ycor()
print(x,y)

#for alphabet A
abc.color("green")
abc.pu()
abc.setpos(127,13.457)
abc.pd()
abc.seth(0)
abc.left(70)
abc.forward(200)
abc.right(150)
abc.forward(200)
x = abc.xcor()
print(x)
abc.right(180)
abc.forward(80)
abc.seth(180)
abc.forward(62)

#for alphabet M
abc.color("yellow")
abc.pu()
abc.setpos(x+10,0)
abc.pd()
abc.seth(90)
abc.forward(200)
abc.right(165)
abc.forward(150)
abc.left(150)
abc.forward(150)
abc.seth(270)
abc.forward(200)

# code for flower design
abc.shape("classic")
abc.color("#DE0CF5")
abc.speed(10)

abc.pu()
abc.setpos(-200,0)
abc.pd()

for i in range(36):
    x=str(random.randint(0,999999))
    if len(x)<6 :
        abc.color("#DE0CF5")
    else:
        abc.color("#"+x)

    abc.left(35)
    abc.forward(50)
    abc.right(35)
    abc.forward(50)
    abc.right(145)
    abc.forward(50)
    abc.right(35)
    abc.forward(50)
    abc.right(10)
    
   
abc.color("#DE0CF5")
abc.seth(270)
abc.forward(200)
window.exitonclick()
