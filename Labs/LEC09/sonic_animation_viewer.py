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
    {'name': 'look_up', 'delay': 0.25, 'frames': [
        (211, 447, 29, 39), (240, 447, 29, 39)]},
    {'name': 'crouch', 'delay': 0.25, 'frames': [
        (270, 448, 24, 32), (302, 448, 29, 26)]},
    {'name': 'walk', 'delay': 0.08, 'frames': [
        (8, 408, 26, 37), (37, 408, 27, 37), (65, 407, 31, 38), (97, 408, 37, 37),
        (135, 410, 32, 35), (170, 408, 32, 38), (206, 408, 26, 38), (238, 408, 24, 37),
        (263, 408, 30, 37), (295, 408, 36, 37), (334, 409, 32, 36), (370, 408, 29, 38)]},
    {'name': 'run', 'delay': 0.07, 'frames': [
        (1, 361, 33, 40), (39, 362, 35, 39), (89, 362, 35, 38), (130, 362, 34, 42)]},
    {'name': 'skid', 'delay': 0.2, 'frames': [
        (181, 362, 34, 41), (228, 363, 33, 40)]},
    {'name': 'spin', 'delay': 0.07, 'frames': [
        (1, 326, 29, 30), (35, 327, 29, 31), (67, 327, 30, 29), (98, 327, 31, 29),
        (131, 327, 29, 30), (162, 326, 29, 31), (193, 326, 30, 29), (230, 326, 31, 29),
        (268, 325, 30, 30)]},
    {'name': 'spin_dash', 'delay': 0.07, 'frames': [
        (1, 292, 30, 27), (36, 292, 29, 27), (70, 292, 29, 27), (105, 292, 29, 27),
        (139, 292, 29, 27), (174, 292, 29, 27)]},
    {'name': 'dash', 'delay': 0.08, 'frames': [
        (1, 251, 29, 35), (36, 251, 30, 35), (74, 251, 31, 35), (111, 251, 31, 36),
        (149, 251, 30, 35), (186, 251, 31, 36)]},
    {'name': 'peel_out', 'delay': 0.08, 'frames': [
        (1, 207, 29, 35), (36, 207, 30, 35), (72, 208, 39, 31), (123, 208, 39, 32),
        (172, 208, 39, 31), (218, 208, 38, 32)]},
    {'name': 'turn', 'delay': 0.12, 'frames': [
        (1, 154, 24, 45), (31, 154, 29, 44), (65, 154, 20, 44), (90, 155, 25, 43),
        (119, 155, 25, 43), (149, 154, 20, 44)]},
    {'name': 'tumble', 'delay': 0.2, 'frames': [
        (184, 156, 40, 28), (232, 157, 39, 27)]},
    {'name': 'push', 'delay': 0.15, 'frames': [
        (1, 108, 27, 38), (31, 110, 31, 36), (64, 110, 31, 36)]},
    {'name': 'board', 'delay': 0.1, 'frames': [
        (99, 110, 33, 38), (136, 110, 32, 36), (176, 110, 33, 36), (217, 110, 33, 36),
        (254, 111, 33, 36)]},
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
    # 모든 동작을 차례로 재생하고, 끝나면 처음부터 다시 반복
    for anim in ANIMATIONS:
        if not running:
            break
        play(anim)

close_canvas()
