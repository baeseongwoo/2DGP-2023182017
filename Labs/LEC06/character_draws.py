# 실습 과제 진행
from pico2d import*
from math import*

open_canvas(800,600)
character = load_image('character.png')

x=400
y=300
def move_circle():
    print("원")
    for degree in range(0,360,1):
        thetha=radians(degree)
        x1=x+150*cos(thetha)
        y1=y+150*sin(thetha)
        draw_character(x1, y1)
    pass

def move_rectangle():
    print("사각형")
    move_bottom()
    move_right()
    move_top()
    move_left()
    pass

def move_triangle():
    print("삼각형")
    move_triangle_left()
    move_triangle_right()
    move_triangle_bottom()
    pass

def draw_character(x, y):
    print("캐릭터 그리기")
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.01)

def move_bottom():
    for x in range(200,601,2):
        draw_character(x,200)

def move_right():
    for y in range(200,401,2):
        draw_character(600,y)

def move_top():
    for x in range(600,199,-2):
        draw_character(x,400)

def move_left():
    for y in range(400,199,-2):
        draw_character(200,y)

def move_triangle_left():
    for t in range(0,100,):
        x=200+(400-200)*t/100
        y=200+(400-200)*t/100
        draw_character(x,y)

def move_triangle_right():
    for t in range(100):
        x=400+(600-400)*t/100
        y=400+(200-400)*t/100
        draw_character(x,y)

def move_triangle_bottom():
    for t in range(100):
        x=600+(200-600)*t/100
        draw_character(x,200)

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()