from pico2d import *

import game_framework
import game_world
import item_mode
import pause_mode
import title_mode
from boy import Boy
from grass import Grass

boy = None


def init():
    global boy
    grass = Grass()
    game_world.add_oject(grass, 0)

    boy = Boy()
    game_world.add_oject(boy, 1)


def finish():
    game_world.clear()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(item_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        else:
            boy.handle_event(event)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


paused_at = 0.0


def pause():
    global paused_at
    paused_at = get_time()
    # 아이템 창/일시정지 중에는 눌려 있던 방향키 상태를 버려서 멈춘 채로 대기
    boy.reset_input()


def resume():
    # 멈춰 있던 시간은 잠들기까지의 대기 시간(5초)에 포함하지 않는다
    boy.idle_started_at += get_time() - paused_at
