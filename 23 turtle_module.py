import turtle

pen=turtle.Turtle()
pen.up()
pen.setposition(-200,200)
pen.down()

def curve_l(x):
    for i in range(x):
        pen.forward(1)
        pen.left(1)

def curve_r(x):
    for i in range(x):
        pen.forward(1)
        pen.right(1)
def random(x):
    for i in range(x):
        pen.forward(10)
        curve_r(200)
        pen.forward(20)
        curve_l(200)
        pen.forward(30)
        curve_r(20)
        curve_r(40)
        curve_l(90)
        pen.right(90)
        pen.forward(2)
        curve_r

random(6)


turtle.done()