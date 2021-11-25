from os import readlink
import turtle as t
from random import randrange, choice
from math import *

DELAY = 10
CSPREAD = 1
COLORS = []

def f1():
    t.speed(15)
    t.color('black')
    for _ in range(sn):
        angl = randrange(20, 150)
        t.setpos(randrange(-CSPREAD, CSPREAD), randrange(-CSPREAD, CSPREAD))
        t.begin_fill()
        t.pendown()
        screen_save(step, angl, randrange(depth // 2, depth * 3))
        t.penup()

    t.penup()
    t.end_fill()
    t.color('white')
    t.setpos(-t.window_width(), t.window_height())
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(8):
        t.begin_fill()
        t.forward(t.window_width() * 2)
        t.right(90)
        t.forward(t.window_height()//10)
        t.right(90)
        t.forward(t.window_width() * 2)
        t.left(90)
        t.forward(t.window_height()//10)
        t.left(90)
        t.delay(DELAY)
        t.end_fill()

    for _ in range(8):
        t.begin_fill()
        t.forward(t.window_width() * 2)
        t.left(90)
        t.forward(t.window_height()//10)
        t.left(90)
        t.forward(t.window_width() * 2)
        t.right(90)
        t.forward(t.window_height()//10)
        t.right(90)
        t.delay(DELAY)
        t.end_fill()
    t.end_fill()
    t.setpos(0, 0)
    t.clear()

    f1()


def f2():
    for i in range(3):
        fractal(step, angl, depth-1, i + 1)

def screen_save(x, a, depth):
    if depth > 0:
        screen_save(x // 2, a, depth-1)

    a = randrange(a // 2, a * 3)
    t.forward(x)

    t.left(a)
    t.forward(x)

    t.right(a)
    t.forward(x)

    t.left(180 - a)
    t.forward(x)

    t.end_fill()
    t.fillcolor(choice(COLORS))
    t.begin_fill()

def fractal(x, a, depth, n):
    print(x, a, depth, n)
    if depth > 0:
        for i in range(3):
            fractal(x/3, angl, depth - 1, i + 1)

    if n == 1:
        print('first')
        pos1 = -step - cos(a * pi/180)*step
        t.setpos(pos1, 0)
        t.forward(x)

    if n == 2:
        print('second')
        pos2 = -cos(a * pi/180)*step
        t.setpos(pos2, 0)
        t.left(a)
        t.forward(x)
        t.right(a)
        t.forward(x)

    if n == 3:
        print('third')
        pos3 = step + cos(a * pi/180)*step
        t.setpos(pos3, 0)
        t.forward(x)



w, h = 1300, 1300
screen = t.Screen()
screen.setup(w, h)
screen.title("Screen Saver")
# screen.bgcolor("blue") # debug purpose

f = open('light.txt')
# screen.bgcolor(f.readline())

for line in f:
    COLORS.extend(f.readline().split())


depth = 3
sn = 10
step = 300
angl = 60

t.hideturtle()
t.speed(1)

f1()
# f2()


t.setpos(0, 0)

t.done()