from pico2d import *
import pico2d.pico2d as p2d

# 스프라이트 시트 출처: DS Naruto Shippuden: Ninja Council 4 - Naruto (The Spriters Resource)

CANVAS_W, CANVAS_H = 1000, 700
GROUND_Y = 120          # 캐릭터 발이 닿는 화면 y좌표
LOOP_COUNT = 5          # 애니메이션별 반복 횟수
PAUSE_TIME = 1.0        # 애니메이션 사이 정지 시간(초)
BG_COLOR = (0, 128, 0)  # 시트의 초록 배경색 -> 투명 처리


# 한 스텝 = 동시에 그릴 스프라이트 목록 (left, bottom, width, height, dx, dy)
def make_steps(rects):
    # 일반 동작: 프레임마다 크기가 달라도 가로 중앙 정렬,
    # 세로는 시트상의 높이 차이(점프 착지 등)를 유지하도록 가장 낮은 bottom을 땅으로 맞춤
    base = min(b for l, b, w, h in rects)
    return [[(l, b, w, h, -w / 2, b - base)] for l, b, w, h in rects]


# 오오다마 라센간 공격용 스프라이트
# 기준점 = 라센간이 땅에 닿는 지점, 나루토는 그 왼쪽 BALL_X 만큼 떨어져 있음
BALL_X = 107
FEET = 1418  # 내려찍기 프레임에서 나루토 발이 있는 시트상의 bottom

CHARGE = [(l, b, w, h, -BALL_X, 0) for l, b, w, h in
          [(32, 1624, 114, 80), (168, 1624, 110, 78), (308, 1624, 114, 73), (449, 1624, 110, 79)]]
SLAM = [(l, b, w, h, -BALL_X, b - FEET) for l, b, w, h in
        [(30, 1418, 115, 80), (171, 1413, 111, 96), (316, 1413, 148, 127), (493, 1411, 168, 133)]]
ATTACK_STEPS = (
    [[c] for c in CHARGE] +     # 1) 라센간 모으기
    [[s] for s in SLAM]         # 2) 내려찍기
)

ANIMATIONS = [
    {'name': 'stance', 'scale': 6, 'delay': 0.12, 'steps': make_steps(
        [(25, 5394, 43, 58), (82, 5394, 43, 56), (140, 5394, 43, 55),
         (196, 5394, 43, 55), (251, 5394, 43, 56), (309, 5394, 43, 57)])},
    {'name': 'walk', 'scale': 6, 'delay': 0.1, 'steps': make_steps(
        [(28, 5281, 23, 60), (65, 5281, 38, 59), (118, 5282, 36, 58),
         (170, 5282, 23, 59), (207, 5281, 36, 59), (258, 5281, 31, 59)])},
    {'name': 'run', 'scale': 6, 'delay': 0.08, 'steps': make_steps(
        [(386, 5281, 44, 48), (442, 5287, 58, 43), (517, 5283, 50, 48),
         (581, 5283, 41, 46), (633, 5287, 55, 45), (703, 5281, 52, 49)])},
    {'name': 'jump', 'scale': 6, 'delay': 0.15, 'steps': make_steps(
        [(24, 5046, 34, 63), (73, 5046, 34, 63), (140, 5046, 49, 64),
         (203, 5046, 49, 63), (277, 5035, 31, 43)])},
    {'name': 'attack', 'scale': 5, 'delay': 0.15, 'steps': ATTACK_STEPS},
]


def load_image_colorkey(path, color):
    # load_image()는 초록 배경을 그대로 그리므로, SDL 컬러키로 배경색을 투명하게 만들어 텍스처 생성
    surface = IMG_Load(path.encode('utf-8'))
    if not surface:
        raise IOError('cannot load %s' % path)
    SDL_SetColorKey(surface, SDL_TRUE, SDL_MapRGB(surface.contents.format, *color))
    texture = SDL_CreateTextureFromSurface(p2d.renderer, surface)
    SDL_FreeSurface(surface)
    return Image(texture)


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_step(anim, step):
    scale = anim['scale']
    clear_canvas()
    for left, bottom, w, h, dx, dy in step:
        x = CANVAS_W // 2 + dx * scale
        y = GROUND_Y + dy * scale
        sheet.clip_draw_to_origin(left, bottom, w, h, x, y, w * scale, h * scale)
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
        for step in anim['steps']:
            if not running:
                return
            handle_events()
            draw_step(anim, step)
            delay(anim['delay'])
    wait(PAUSE_TIME)


open_canvas(CANVAS_W, CANVAS_H)
sheet = load_image_colorkey('naruto_sheet.png', BG_COLOR)

running = True
while running:
    for anim in ANIMATIONS:
        if not running:
            break
        play(anim)

close_canvas()
