#Jonas York
#U3 Project
#Making a tree with recurison and turtle. ughhhhhhhhhhhhhhhhhhh

#I'm not looking forward to this

"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""

import turtle
import random
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(200)
t.pendown()
t.pensize(3)
t.speed(10)
ROTATE = 30
LENGTH = 100
SIZE = 10
LEAFLENGTH = 10
LEAFSIZE = 8

def drawTree(length,thickness): #note: is should be done in 10 length intervals 
  if length == 10:
    draw_leaf()
    return None
  ROTATE=random.randint(1,69)
  branches = random.randint(0,2)
  t.color("Brown")
  t.pensize(thickness)
  t.forward(length)
  t.right(ROTATE)
  drawTree(length-10,thickness-1)
  t.left(ROTATE)  
  t.left(ROTATE)
  drawTree(length-10,thickness-1)
  t.right(ROTATE)
  t.backward(length)



def draw_leaf():
    t.color("Green")
    t.pensize(LEAFSIZE)
    t.forward(LEAFLENGTH)
    t.backward(LEAFLENGTH)
    t.pensize(1)
    t.color("Brown")

  
def main():
  drawTree(LENGTH, SIZE)

if __name__ == "__main__":
  main()






turtle.mainloop()

#backup code in case it fails 
# import turtle
# t = turtle.Turtle()
# t.left(90)
# t.penup()
# t.backward(200)
# t.pendown()
# t.pensize(3)
# t.speed(10)
# ROTATE = 30
# LENGTH = 100
# SIZE = 10
# LEAFLENGTH = 10
# LEAFSIZE = 8

# def drawTree(length,thickness): #note: is should be done in 10 length intervals 
#   if length == 10:
#     draw_leaf()
#     return None
#   t.color("Brown")
#   t.pensize(thickness)
#   t.forward(length)
#   t.right(ROTATE)
#   drawTree(length-10,thickness-1)
#   t.left(ROTATE*2)  

#   drawTree(length-10,thickness-1)
#   t.right(ROTATE)
#   t.backward(length)



# def draw_leaf():
#     t.color("Green")
#     t.pensize(LEAFSIZE)
#     t.forward(LEAFLENGTH)
#     t.backward(LEAFLENGTH)
#     t.pensize(1)
#     t.color("Brown")

  
# def main():
#   drawTree(LENGTH, SIZE)

# if __name__ == "__main__":
#   main()


