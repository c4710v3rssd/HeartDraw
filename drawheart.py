import turtle

pen=turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
        
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    
def text():
    pen.up()
    pen.setpos(-60,95)
    pen.down()
    pen.color('white')
    pen.write("I Love You <3")
    
heart()
text()
pen.ht()   

#c4710v3r         