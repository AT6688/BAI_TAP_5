import turtle
import luoi

t = turtle.Turtle()
# luoi.make_grid(t)

turtle.bgcolor("#F0F8FF")
t.color("black")
t.pensize(3)
t.hideturtle()

#ve hinh mat truoc cua nha
t.color("#FFDEAD")
t.begin_fill()
t.penup()
t.goto(-120,0)
t.pendown()
t.fd(240)
t.lt(90)
t.fd(120)
t.lt(90)
t.fd(240)
t.lt(90)
t.fd(120)
t.end_fill()

#ve cua cua nha
t.color("#191970")
t.begin_fill()
t.penup()
t.goto(-40,0)
t.pendown()
t.lt(90)
t.fd(80)
t.lt(90)
t.fd(80)
t.lt(90)
t.fd(80)
t.lt(90)
t.fd(80)
t.end_fill()


#ve mai nha hinh tam giac
t.color("#B22222")
t.begin_fill()
t.penup()
t.goto(-120,120)
t.pendown()
t.goto(40,120)
t.goto(-40,200)
t.goto(-120,120)
t.end_fill()


#ve ong khoi
t.color("#800000")
t.begin_fill()
t.penup()
t.goto(0,160)
t.pendown()
t.goto(0,240)
t.goto(20,240)
t.goto(20,140)
t.goto(0,160)
t.end_fill()

#khoi
t.penup()
t.goto(20,260)
t.pendown()
t.goto(20,320)
t.penup()
t.goto(10,260)
t.pendown()
t.goto(10,300)

#hung nang
t.color("#1E90FF")
t.begin_fill()
t.penup()
t.goto(50,120)
t.pendown()
t.circle(30,-180)
t.goto(50,120)
t.end_fill()


#ve cay co thu
t.color("#8B4513")
t.begin_fill()
t.penup()
t.goto(240,-80)
t.pendown()
t.goto(320,-80)
t.goto(300,40)
t.goto(260,40)
t.goto(240,-80)
t.end_fill()

t.color("#006400")
t.begin_fill()
t.penup()
t.goto(200,40)
t.pendown()
t.goto(360,40)
t.goto(280,120)
t.goto(200,40)
t.end_fill()

t.color("#9ACD32")
t.begin_fill()
t.penup()
t.goto(220,120)
t.pendown()
t.goto(340,120)
t.goto(280,180)
t.goto(220,120)
t.end_fill()

t.color("#FFD700")
t.begin_fill()
t.penup()
t.goto(240,180)
t.pendown()
t.goto(320,180)
t.goto(280,220)
t.goto(240,180)
t.end_fill()

#mat troi
t.color("#FFA500")
t.begin_fill()
t.penup()
t.goto(-200,320)
t.pendown()
t.circle(20)
t.end_fill()

t.color("black")

#nguoi tuyet

t.penup()
t.goto(-200,0)
t.pendown()
t.circle(80,180)
t.goto(-200,0)



t.penup()
t.goto(-320,120)
t.pendown()
t.circle(40)

t.penup()
t.goto(-305,130)
t.pendown()
t.circle(5)

t.penup()
t.goto(-265,130)
t.pendown()
t.circle(5)

#mieng
t.penup()
t.goto(-300,100)
t.pendown()
t.goto(-260,100)

#mui
t.color("#FFA500")
t.begin_fill()
t.penup()
t.goto(-280,120)
t.pendown()
t.goto(-285,110)
t.goto(-275,110)
t.goto(-280,120)
t.end_fill()

t.color("black")

t.penup()
t.goto(-220,50)
t.pendown()
t.goto(-180,100)

t.penup()
t.goto(-220,50)
t.pendown()
t.goto(-180,100)
t.circle(10)

t.penup()
t.goto(-340,50)
t.pendown()
t.goto(-380,40)
t.penup()
t.goto(-400,40)
t.pendown()
t.circle(10,-360)


turtle.done()