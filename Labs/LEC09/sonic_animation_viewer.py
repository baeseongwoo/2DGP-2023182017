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


def draw_frame(frame):
    # 가로는 화면 중앙에 프레임 중앙을, 세로는 프레임 아래쪽을 바닥선에 맞춘다
    left, bottom, w, h = frame
    x = CANVAS_W // 2 - w * SCALE // 2
    clear_canvas()
    sheet.clip_draw_to_origin(left, bottom, w, h, x, GROUND_Y, w * SCALE, h * SCALE)
    update_canvas()


open_canvas(CANVAS_W, CANVAS_H)
sheet = load_image('sonic-sprite.png')

running = True
while running:
    handle_events()
    draw_frame((1, 447, 29, 39))
    delay(0.05)

close_canvas()
