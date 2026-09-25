# 실습 과제 진행
from pico2d import*

open_canvas(800,600)
character = load_image('character.png')

clear_canvas()
character.draw(400,300)
update_canvas()

x=400
y=300


def move_circle():
    print("원")
    draw_character(400, 300)
    pass

def move_rectangle():
    print("사각형")
    draw_character(400, 300)

    pass

def move_triangle():
    print("삼각형")
    draw_character(400, 300)
    pass

def draw_character(x, y):
    print("캐릭터 그리기")
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    

while True:
    move_circle()

    move_rectangle()

    move_triangle()
    pass

close_canvas()