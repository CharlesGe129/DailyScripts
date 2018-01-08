# coding=utf-8
import turtle


def left(degree):
    turtle.left(degree)


def right(degree):
    turtle.right(degree)


def forward(distance):
    turtle.forward(distance)


def petal(params):
    left(params[0])
    turtle.circle(params[1][0], params[1][1])
    left(params[2])
    turtle.circle(params[3][0], params[3][1])
    left(params[4])
    turtle.circle(params[5][0], params[5][1])


turtle.speed(10)
turtle.pensize(5)
turtle.pencolor("pink")
turtle.screensize(bg='red')

# First half
left(150)
turtle.circle(7, 190)
turtle.circle(20, 200)
turtle.circle(10, 60)

# Second half
turtle.penup()
left(40)
forward(35)
turtle.pendown()
left(160)
forward(20)
turtle.circle(13, 90)
turtle.circle(50, 55)
turtle.left(70)
turtle.circle(50, 25)
turtle.left(10)
turtle.circle(70, 40)
# 3
petal([30, [70, 70], 70, [70, 60], 180, [-70, 35]])

# 4
petal([90, [60, 70], 70, [60, 75], 180, [-60, 40]])

# 5
petal([70, [60, 70], 70, [60, 65], 180, [-60, 35]])

# 6
petal([70, [60, 70], 70, [60, 70], 180, [-60, 25]])

# 7
petal([50, [60, 70], 70, [60, 50], 180, [-60, 15]])

# 7
petal([50, [60, 70], 70, [60, 55], 180, [-60, 20]])

# 8
petal([50, [60, 70], 70, [60, 55], 180, [-60, 15]])

# 9
petal([40, [60, 70], 70, [60, 80], 180, [-60, 35]])

# 10
petal([40, [60, 70], 70, [60, 45], 180, [-60, 15]])

# 11
petal([40, [60, 70], 70, [60, 85], 180, [-60, 50]])

# 12
petal([40, [60, 70], 70, [60, 65], 180, [-60, 35]])

# 13
petal([40, [60, 70], 70, [60, 85], 180, [-60, 40]])

# 14
petal([20, [60, 70], 70, [60, 60], 180, [-60, 10]])

# 15
petal([30, [60, 60], 70, [60, 75], 180, [-60, 40]])

# 16
petal([30, [60, 70], 70, [60, 55], 180, [-60, 25]])

# 17
petal([40, [60, 50], 70, [60, 90], 180, [-60, 50]])

# 18
petal([30, [60, 70], 70, [60, 80], 180, [-60, 40]])

# 19
petal([60, [60, 70], 50, [60, 85], 180, [-60, 45]])

# 20
petal([45, [60, 55], 50, [60, 60], 180, [-60, 45]])

turtle.mainloop()
