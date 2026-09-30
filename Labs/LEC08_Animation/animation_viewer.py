from pico2d import *
import pico2d.pico2d as p2d

# 스프라이트 시트 출처: DS Naruto Shippuden: Ninja Council 4 - Naruto (The Spriters Resource)

CANVAS_W, CANVAS_H = 800, 600
GROUND_Y = 100          # 캐릭터 발이 닿는 화면 y좌표
SCALE = 6               # 확대 배율 (캐릭터가 화면 높이의 절반 이상)
LOOP_COUNT = 5          # 애니메이션별 반복 횟수
PAUSE_TIME = 1.0        # 애니메이션 사이 정지 시간(초)
BG_COLOR = (0, 128, 0)  # 시트의 초록 배경색 -> 투명 처리

# 프레임마다 크기가 다르므로 (left, bottom, width, height)를 프레임별로 저장
# bottom은 pico2d 기준(이미지 아래쪽에서부터의 거리)
ANIMATIONS = [
    {
        'name': 'stance',
        'frames': [(25, 5394, 43, 58), (82, 5394, 43, 56), (140, 5394, 43, 55),
                   (196, 5394, 43, 55), (251, 5394, 43, 56), (309, 5394, 43, 57)],
    },
    {
        'name': 'walk',
        'frames': [(28, 5281, 23, 60), (65, 5281, 38, 59), (118, 5282, 36, 58),
                   (170, 5282, 23, 59), (207, 5281, 36, 59), (258, 5281, 31, 59)],
    },
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


def draw_frame(anim, frame):
    # 프레임 크기가 달라도 발이 땅에 붙어 있도록 왼쪽 아래 기준으로 그리고, 가로는 중앙 정렬
    left, bottom, w, h = anim['frames'][frame]
    x = CANVAS_W // 2 - w * SCALE // 2
    clear_canvas()
    sheet.clip_draw_to_origin(left, bottom, w, h, x, GROUND_Y, w * SCALE, h * SCALE)
    update_canvas()


def play(anim):
    for _ in range(LOOP_COUNT):
        for frame in range(len(anim['frames'])):
            if not running:
                return
            handle_events()
            draw_frame(anim, frame)
            delay(0.12)
    delay(PAUSE_TIME)


open_canvas(CANVAS_W, CANVAS_H)
sheet = load_image_colorkey('naruto_sheet.png', BG_COLOR)

running = True
while running:
    for anim in ANIMATIONS:
        if not running:
            break
        play(anim)

close_canvas()
