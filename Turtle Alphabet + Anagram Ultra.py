# Project 3- Turtle Alphabet
# If you got help from anyone, please write their emails here:
#  1) acbart@udel.edu
#  2) ...

###############################################################
# Part 1) Setup
# Load turtle module, move it to left side, make turtle faster
import turtle
turtle.reset()
turtle.speed(10)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.speed(3)

###############################################################
# Part 2) Drawing
# Write the code for each letter below

# First letter
# ...
def draw_start(x_pos: int, y_pos: int) -> int:
    turtle.penup()
    turtle.goto(x_pos, y_pos)
    turtle.pendown()         #End of position moving portion
    return None

def draw_a(x_pos: int, y_pos: int) -> int:
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(30)         #End of letter drawing
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()           #End of turtle prep for next letter
    return None

def draw_g(x_pos: int, y_pos: int) -> int:
    turtle.left(90) 
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(30) #End of letter drawing
    turtle.right(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()           #End of turtle prep for next letter
    return None

def draw_r(x_pos: int, y_pos: int) -> int:
    turtle.left(90) 
    turtle.forward(50)
    turtle.right(90) 
    turtle.forward(50)
    turtle.right(90) 
    turtle.forward(25)
    turtle.right(90) 
    turtle.forward(50)
    turtle.left(90) 
    turtle.forward(25)
    turtle.left(180) 
    turtle.forward(25)
    turtle.right(120) 
    turtle.forward(50)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()
    return None

def draw_e(x_pos: int, y_pos: int) -> int:
    turtle.left(90) 
    turtle.forward(50)
    turtle.right(90) 
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()
    return None

def draw_t(x_pos: int, y_pos: int) -> int:
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()
    return None

def draw_i(x_pos: int, y_pos: int) -> int:
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()
    
def draw_m(x_pos: int, y_pos: int) -> int:
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()
    
a_great_time = draw_start(-333, 177)
a_great_time = draw_a(a_great_time, 50)
a_great_time = draw_g(a_great_time, 50)
a_great_time = draw_r(a_great_time, 50)
a_great_time = draw_e(a_great_time, 50)
a_great_time = draw_a(a_great_time, 50)
a_great_time = draw_t(a_great_time, 50)
a_great_time = draw_t(a_great_time, 50)
a_great_time = draw_i(a_great_time, 50)
a_great_time = draw_m(a_great_time, 50)
a_great_time = draw_e(a_great_time, 50)

tiger = draw_start(-13, -87)
tiger = draw_t(tiger, -87)
tiger = draw_i(tiger, -87)
tiger = draw_g(tiger, -87)
tiger = draw_e(tiger, -87)
tiger = draw_r(tiger, -87)

treat = draw_start(-424, -137)
treat = draw_t(treat, -137)
treat = draw_r(treat, -137)
treat = draw_e(treat, -137)
treat = draw_a(treat, -137)
treat = draw_t(treat, -137)
# Second letter
# ...

###############################################################
# Part 3) Wrap-up
# Start the turtles!
turtle.mainloop()
