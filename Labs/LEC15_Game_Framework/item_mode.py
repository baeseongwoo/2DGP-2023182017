from pico2d import *

import game_framework
import game_world
import play_mode

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key in (SDLK_ESCAPE, SDLK_i):
                game_framework.pop_mode()
            elif event.key == SDLK_0:
                play_mode.boy.item = None
                game_framework.pop_mode()
            elif event.key == SDLK_1:
                play_mode.boy.item = 'SmallBall'
                game_framework.pop_mode()
            elif event.key == SDLK_2:
                play_mode.boy.item = 'BigBall'
                game_framework.pop_mode()


def update():
    pass  # 아이템 창이 떠 있는 동안 게임 월드는 멈춘다


def render():
    clear_canvas()
    game_world.render()      # 멈춘 게임 화면을 그대로 배경으로
    image.draw(400, 300)     # 그 위에 아이템 선택 창
    update_canvas()


def pause():
    pass


def resume():
    pass
