from pico2d import *

CANVAS_W, CANVAS_H = 1200, 800
SCALE = 8               # 확대 배율
GROUND_Y = 120          # 발이 닿는 바닥선의 화면 y좌표
LOOP_COUNT = 5          # 동작별 반복 횟수
PAUSE_TIME = 1.0        # 동작 사이 정지 시간(초)

# 프레임 하나 = (left, bottom, width, height)
# 동작 하나 = 이름, 프레임 간 지연 시간(초), 프레임 목록
ANIMATIONS = [
    {'name': 'idle', 'delay': 0.15, 'frames': [
        (1, 447, 29, 39), (31, 447, 26, 38), (58, 447, 29, 39), (87, 447, 29, 39),
        (118, 447, 30, 38), (150, 447, 30, 38), (182, 447, 29, 39)]},
]


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


def wait(seconds):
    # 정지 중에도 창 닫기/ESC가 먹도록 잘게 나눠서 대기
    elapsed = 0.0
    while running and elapsed < seconds:
        handle_events()
        delay(0.05)
        elapsed += 0.05


def play(anim):
    for _ in range(LOOP_COUNT):
        for frame in anim['frames']:
            handle_events()
            if not running:
                return
            draw_frame(frame)
            delay(anim['delay'])
    wait(PAUSE_TIME)


open_canvas(CANVAS_W, CANVAS_H)
sheet = load_image('sonic-sprite.png')

running = True
while running:
    play(ANIMATIONS[0])

close_canvas()
