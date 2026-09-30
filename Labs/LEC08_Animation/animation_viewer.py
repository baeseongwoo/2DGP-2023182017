from pico2d import *
import pico2d.pico2d as p2d

# 스프라이트 시트 출처: DS Naruto Shippuden: Ninja Council 4 - Naruto (The Spriters Resource)

CANVAS_W, CANVAS_H = 800, 600
BG_COLOR = (0, 128, 0)  # 시트의 초록 배경색 -> 투명 처리


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

clear_canvas()
sheet.clip_draw(25, 5394, 43, 58, CANVAS_W // 2, CANVAS_H // 2)
update_canvas()
delay(2)

close_canvas()
