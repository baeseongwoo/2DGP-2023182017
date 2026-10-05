from pico2d import *

CANVAS_W, CANVAS_H = 1200, 800
SCALE = 8               # 확대 배율
GROUND_Y = 120          # 발이 닿는 바닥선의 화면 y좌표


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(CANVAS_W, CANVAS_H)
sheet = load_image('sonic-sprite.png')

running = True
while running:
    handle_events()
    clear_canvas()
    sheet.clip_draw_to_origin(1, 447, 29, 39, 100, 100, 29 * SCALE, 39 * SCALE)
    update_canvas()
    delay(0.05)

close_canvas()
