from pico2d import *

import game_framework
import game_world


def init():
    pass


def finish():
    pass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()


def update():
    pass  # 게임 월드를 업데이트하지 않으므로 소년과 공이 그 자리에서 멈춘다


def render():
    clear_canvas()
    game_world.render()  # 멈춘 순간의 화면을 그대로 그린다
    update_canvas()


def pause():
    pass


def resume():
    pass
