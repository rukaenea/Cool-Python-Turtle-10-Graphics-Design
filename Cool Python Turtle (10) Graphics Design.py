import turtle as t
import colorsys

t.tracer(2)
t.pensize(2)
t.pencolor("gold")
t.setpos(-40,30)
h=0.7
t.bgcolor("black")

def design():
	global h
	for i in range(4):
		c=colorsys.hsv_to_rgb(h,1,1)
		h+=0.004
		t.fillcolor(c)
		t.begin_fill()
		t.fd(100)
		t.rt(30)
		t.fd(100)
		t.right(60)
		t.end_fill()

for j in range(25):
  design()
  t.goto(0,0)
  t.lt(-15)		
t.done()