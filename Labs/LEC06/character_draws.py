# 실습 과제 진행
from pico2d import*

open_canvas(800,600)
character = load_image('character.png')

clear_canvas()
character.draw(400,300)
update_canvas()

def move_circle():
    print("원")
    pass

def move_rectangle():
    print("사각형")
    pass

def move_triangle():
    print("삼각형")
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()