from pico2d import *
import pico2d.pico2d as p2d

# 스프라이트 시트 출처: DS Naruto Shippuden: Ninja Council 4 - Naruto (The Spriters Resource)

CANVAS_W, CANVAS_H = 800, 600
BG_COLOR = (0, 128, 0)  # 시트의 초록 배경색 -> 투명 처리

# stance 프레임 (left, bottom, width, height), bottom은 pico2d 기준(이미지 아래쪽에서부터의 거리)
STANCE = [(25, 5394, 43, 58), (82, 5394, 43, 56), (140, 5394, 43, 55),
          (196, 5394, 43, 55), (251, 5394, 43, 56), (309, 5394, 43, 57)]


def load_image_colorkey(path, color):
    # load_image()는 초록 배경을 그대로 그리므로, SDL 컬러키로 배경색을 투명하게 만들어 텍스처 생성
    surface = IMG_Load(path.encode('utf-8'))
    if not surface:
        raise IOError('cannot load %s' % path)
    SDL_SetColorKey(surface, SDL_TRUE, SDL_MapRGB(surface.contents.format, *color))
    texture = SDL_CreateTextureFromSurface(p2d.renderer, surface)
    SDL_FreeSurface(surface)
    return Image(texture)


open_canvas(CANVAS_W, CANVAS_H)
sheet = load_image_colorkey('naruto_sheet.png', BG_COLOR)

for left, bottom, w, h in STANCE:
    clear_canvas()
    sheet.clip_draw(left, bottom, w, h, CANVAS_W // 2, CANVAS_H // 2)
    update_canvas()
    delay(0.12)

close_canvas()
