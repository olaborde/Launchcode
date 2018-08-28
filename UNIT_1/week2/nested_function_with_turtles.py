import turtle

jack = turtle.Turtle() 

def draw_square(t):
  for x in range(4):
    t.forward(150)
    t.left(90)



def draw_multiple_squares(t, amount):
  for x in range(int(amount)):
    draw_square(t)
    t.forward(50)


draw_multiple_squares(jack, 45)  